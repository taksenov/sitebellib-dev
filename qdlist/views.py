# coding=utf-8
# Create your views here.
from django.db import connection
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from qdlist.models import *

# Вывод меню для выбора среди всех оцифрованных документов
def qdlist(request):
    all_types = connection.cursor()
    all_types.execute ("""
        SELECT * FROM qdlist_type;
    """)
    result_all_types = all_types.fetchall()

    all_subtypes = connection.cursor()
    all_subtypes.execute ("""
        SELECT * FROM qdlist_subtype;
    """)
    result_all_subtypes = all_subtypes.fetchall()

    templ = get_template('QuantDocsIndex.html')
    html = templ.render(Context({'result_all_types': result_all_types,
                                 'result_all_subtypes' : result_all_subtypes,
                                 'user': request.user
                                }))
    return HttpResponse(html)

# Вывод страницы c газетами за нужный год и список газет за год
# Внимание в шаблоне  забит гвоздь для показа оцифрованных
# газет "Белоярские вести" и "Белоярские новости"  и для перехода в шаблон BelNewsTempl.html.
def qdpselect(request, Year):
    """


    :param Year:
    :param request:
    :return:
    """
    try:
        Year = int(Year)
    except ValueError:
        raise Http404()

# если в url указан год которого нет в таблице, то вызвать страницу 404
    if Year not in years.objects.all().values_list('Year_id', flat=True):
        raise Http404()
# ============================================================================

    qdlist = connection.cursor()
    qdlist.execute("""
        SELECT qdlist_name.NameDocumentFull
            ,qdlist_quantizeddoc.QDDate
            ,qdlist_quantizeddoc.QDNumSerial
            ,qdlist_quantizeddoc.QDNumFromPublication
            ,qdlist_links.DomainLinkName
            ,qdlist_name.NameDocument
            ,qdlist_quantizeddoc.QDNumExtra
        FROM qdlist_quantizeddoc
            ,qdlist_links
            ,qdlist_name
            ,qdlist_years
        WHERE 1=1
            AND qdlist_years.year_id = %s
            AND qdlist_quantizeddoc.year_id = qdlist_years.year_id
            AND qdlist_quantizeddoc.name_id = qdlist_name.name_id
            AND qdlist_quantizeddoc.link_id = qdlist_links.link_id
        ORDER BY qdlist_quantizeddoc.QDDate;
        """, [Year])                    # Year
    resultsqdlist = qdlist.fetchall()                                           # список газет за 1989 год
    templ = get_template('BelNewsTempl.html')
    html = templ.render(Context({'resultsqdlist': resultsqdlist,
                                 'Year': Year,
                                 'user': request.user
                                }))
    return HttpResponse(html)

def qdspersonal(request):
    resultsqdlist = connection.cursor()
    resultsqdlist.execute ("""
    SELECT  l.DomainLinkname
           ,st.linktypename
           ,n.NameDocument
    FROM  qdlist_name n
         ,qdlist_links l
         ,qdlist_quantizeddoc qd
         ,qdlist_subtype st
    WHERE 1=1
    AND n.Name_id not in (1, 2)
    AND n.Name_id = qd.Name_id
    AND l.Link_id = qd.Link_id
    ;
    """)
    resultsqdlist = resultsqdlist.fetchall()
    templ = get_template('QuantDocsTempl.html')
    html = templ.render(Context({'resultsqdlist': resultsqdlist,
                               'user': request.user
                                }))
    return HttpResponse(html)