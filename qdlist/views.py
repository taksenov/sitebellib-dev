# coding=utf-8
# Create your views here.
from django.db import connection
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from qdlist.models import *


# Вывод страницы c газетами за нужный год и список газет за год
def qdlist(request, Year):
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