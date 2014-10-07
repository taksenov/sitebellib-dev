__author__ = 'taksenov'
# coding=utf-8

# imports
from django.db import connection
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext




# Вывод новостей
def vknewsView(request):
    last10newses = connection.cursor()
    last10newses.execute ("""
        SELECT q.*
        FROM   vknews_vknews q
        ORDER BY q.id DESC LIMIT 10
        ;
    """)
    result_last10newses = last10newses.fetchall()

    # Внимание! Если хочешь не иметь проблем с CSRF
    # то везде используй RequestContext!
    templ = get_template('vknews.html')
    html = templ.render(
                        RequestContext(request,
                                       {
                                       'result_last10newses': result_last10newses,
                                       'user': request.user,
                                       }
                                       )
                       )
    return HttpResponse(html)