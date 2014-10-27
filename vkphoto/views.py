__author__ = 'taksenov'
# coding=utf-8

# imports
from django.db import connection
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext




# Вывод новостей
def vkphotoView(request):
    last30photoes = connection.cursor()
    last30photoes.execute ("""
        SELECT q.*
        FROM   vkphoto_vknews q
        ORDER BY q.id DESC LIMIT 30
        ;
    """)
    result_last10newses = last30photoes.fetchall()

    # фотогалерея
    header = 'Фотогалерея'
    # Все самые интересные новости и события из жизни наших библиотек
    subheader = 'Фотографии рассказывающие о событиях из жизни наших библиотек'

    # Берем шаблон от vknews (повтороное использование кода), поэтому такое странное название переменных с данными
    # Внимание! Если хочешь не иметь проблем с CSRF
    # то везде используй RequestContext!
    templ = get_template('vknews.html')
    html = templ.render(
                        RequestContext(request,
                                       {
                                       'result_last10newses': result_last10newses,
                                       'user': request.user,
                                       'header':header,
                                       'subheader':subheader,
                                       }
                                       )
                       )
    return HttpResponse(html)