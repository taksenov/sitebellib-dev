__author__ = 'taksenov'
# coding=utf-8

# imports
from django.db import connection
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context




# Вывод меню для выбора среди всех оцифрованных документов
def prolongMain(request):
    all_libs = connection.cursor()
    all_libs.execute ("""
        SELECT * FROM new_www_book_base.elcat_library;
    """)
    result_all_libs = all_libs.fetchall()


    templ = get_template('prolong.html')
    html = templ.render(Context({'result_all_libs': result_all_libs,
                                 'user': request.user
                                }))
    return HttpResponse(html)