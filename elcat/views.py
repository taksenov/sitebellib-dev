# coding: utf-8

from sphinxapi import *
import sys
from django.db import connection
from django.http import Http404, HttpResponse, HttpRequest
from django.template.loader import get_template
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from elcat.models import *

# Вывод страницы c формой поиска в электронном каталоге
def elcat_index(request):
    return render_to_response('ElcatIndex.html', {'current_path': request.path, 'user': request.user}, RequestContext(request, {}))

# форма с результатами поиска
def elcat_search(request):
    if 'q' in request.GET and request.GET['q']:
        # Подключаемся к sphinxd используя sphinxapi.py
        cl = SphinxClient()
        cl.SetServer('127.0.0.1', 9312)
        # режим поиска совпадений
        cl.SetMatchMode(SPH_MATCH_BOOLEAN)
        cl.SetSortMode(SPH_SORT_RELEVANCE)
        res = cl.Query(request.GET['q'])

        if not res:
            SearchResult = 'Поиск не дал результатов. Пожалуйста, попробуйте поменять условия вашего запроса.'
            sr_id = 0

        # Собираем id книг и авторов и маркеры этих id в словарь data
        data = {}
        if res.has_key('matches'):
            n = 1
            sr_id = 1
            for match in res['matches']:
                data[n] = {'id' : match['id'] , 'row_type' : match['attrs']['row_type']}
                n += 1

        # Создаю два пустых списка и произвожу их заполнение id книг и id авторов с row_type = 1
        # и row_type = 2 соотвественно
        datar1 = []
        datar2 = []
        i = 0
        for key in data:
            a = data[key]['row_type']
            if a == 1:
                datar1.insert(i, data[key]['id'])
            elif a == 2:
                datar2.insert(i, data[key]['id'])
            i += 1

        # Две переменные ниже нужны для того чтобы запрос отработал в любом случае, даже если
        # нет или авторов или книг в поиске
        r1 = 0
        r2 = 0

        # еще один костыль, если в поиске по книге или по автору будет одно совпадение, то почему-то
        # в sql запрос строка уходит с запятой на конце, чтобы этого не случилось всегда
        # в таких случаях добавляю нулевой id и в запрос строка уйдет в нормальном виде
        if len(datar1) == 1:
            datar1.append(0)
        if len(datar2) == 1:
            datar2.append(0)

        if len(datar1) != 0:
            r1 = 1
            # Выборка книг по найденным в поиске id книг (row_type = 1)
            elcat_search_r1 = connection.cursor()
            elcat_search_r1.execute(

                """
                #Вывод данных о книге по ее id (row_type = 1)
                SELECT  a.Name           AS Author         #автор книги
                       ,b.Name           AS BookName       #название книги
                       ,b.Inventory                        #инвентарный номер книги
                       ,bbk1.Code1       AS BBK1           #ББК 1
                       ,bbk2.Code2       AS BBK2           #ББК 2
                       ,p.Name           AS Publisher      #издательсто
                       ,p.City                             #город издательства
                       ,b.Year                             #год издания книги
                       ,b.Pages                            #количество страниц
                       ,b.ISBN                             #ISBN
                       ,g.Name           AS Genre          #жанр
                       ,ser.Name         AS Series         #серия
                       ,l.Name           AS Language       #язык
                       ,shp.Name         AS ShelfPlace     #место на полке
                       ,lib.Name         AS Library        #библиотека
                       ,lt.Town                            #населденный пункт библиотеки
                       ,c.Name           AS Content        #тип контента
                       ,b.Price          AS Price          #цена
                FROM  elcat_book           b
                     ,elcat_author         a
                     ,elcat_publisher      p
                     ,elcat_bbk1           bbk1
                     ,elcat_bbk2           bbk2
                     ,elcat_language       l
                     ,elcat_library        lib
                     ,elcat_content        c
                     ,elcat_genre          g
                     ,elcat_series         ser
                     ,elcat_shelfplace     shp
                     ,elcat_librarytown    lt
                     ,elcat_book_author_id ba
                WHERE 1=1
                      AND b.Book_id        in %s
                      AND ba.book_id       = b.Book_id
                      AND ba.author_id     = a.author_id
                      AND b.Bbk1_id        = bbk1.Bbk1_id
                      AND b.Bbk2_id        = bbk2.Bbk2_id
                      AND b.Genre_id       = g.Genre_id
                      AND b.Series_id      = ser.Series_id
                      AND b.Content_id     = c.Content_id
                      AND b.Publisher_id   = p.Publisher_id
                      AND b.Language_id    = l.Language_id
                      AND b.ShelfPlace_id  = shp.ShelfPlace_id
                      AND b.Library_id     = lib.Library_id
                      AND b.LibraryTown_id = lt.LibraryTown_id
                      #! Следить за тем списана ли книга (b.isdeleted != 1)
                      AND b.isdeleted      = 0
                ;
                """ , [datar1] )

        if len(datar2) != 0:
            r2 = 1
            # Выборка всех книг конкретного автора, по найденным в поиске id авторов (row_type = 2)
            elcat_search_r2 = connection.cursor()
            elcat_search_r2.execute(

                """
                #Вывод данных о всех книгах по id автора (row_type = 2)
                SELECT  a.Name           AS Author         #автор книги
                       ,b.Name           AS BookName       #название книги
                       ,b.Inventory                        #инвентарный номер книги
                       ,bbk1.Code1       AS BBK1           #ББК 1
                       ,bbk2.Code2       AS BBK2           #ББК 2
                       ,p.Name           AS Publisher      #издательсто
                       ,p.City                             #город издательства
                       ,b.Year                             #год издания книги
                       ,b.Pages                            #количество страниц
                       ,b.ISBN                             #ISBN
                       ,g.Name           AS Genre          #жанр
                       ,ser.Name         AS Series         #серия
                       ,l.Name           AS Language       #язык
                       ,shp.Name         AS ShelfPlace     #место на полке
                       ,lib.Name         AS Library        #библиотека
                       ,lt.Town                            #населденный пункт библиотеки
                       ,c.Name           AS Content        #тип контента
                       ,b.Price          AS Price          #цена
                FROM  elcat_book           b
                     ,elcat_author         a
                     ,elcat_publisher      p
                     ,elcat_bbk1           bbk1
                     ,elcat_bbk2           bbk2
                     ,elcat_language       l
                     ,elcat_library        lib
                     ,elcat_content        c
                     ,elcat_genre          g
                     ,elcat_series         ser
                     ,elcat_shelfplace     shp
                     ,elcat_librarytown    lt
                     ,elcat_book_author_id ba
                WHERE 1=1
                      AND a.Author_id      in %s
                      AND ba.book_id       = b.Book_id
                      AND ba.author_id     = a.author_id
                      AND b.Bbk1_id        = bbk1.Bbk1_id
                      AND b.Bbk2_id        = bbk2.Bbk2_id
                      AND b.Genre_id       = g.Genre_id
                      AND b.Series_id      = ser.Series_id
                      AND b.Content_id     = c.Content_id
                      AND b.Publisher_id   = p.Publisher_id
                      AND b.Language_id    = l.Language_id
                      AND b.ShelfPlace_id  = shp.ShelfPlace_id
                      AND b.Library_id     = lib.Library_id
                      AND b.LibraryTown_id = lt.LibraryTown_id
                      #! Следить за тем списана ли книга (b.isdeleted != 1)
                      AND b.isdeleted      = 0
                ;
                """ , [datar2] )

        if r1 == 0 and r2 == 0:
             return render_to_response('ElcatSearchNoResults.html', {'user': request.user})
        elif r1 == 0:
            resultselcat_search = elcat_search_r2.fetchall()
            templ = get_template('ElcatSearch.html')
            html = templ.render(Context({'resultselcat_search': resultselcat_search,
                                         'user': request.user
                                        }))
        elif r2 == 0:
            resultselcat_search = elcat_search_r1.fetchall()
            templ = get_template('ElcatSearch.html')
            html = templ.render(Context({'resultselcat_search': resultselcat_search,
                                         'user': request.user
                                        }))
        elif r1 == 1 and r2 == 1:
            resultselcat_search = elcat_search_r1.fetchall() + elcat_search_r2.fetchall()
            templ = get_template('ElcatSearch.html')
            html = templ.render(Context({'resultselcat_search': resultselcat_search,
                                         'user': request.user
                                        }))

    else:
         return render_to_response('ElcatSearchNoResults.html', {'user': request.user})

    # возвращает общую страницу с результатами поискового запроса
    return HttpResponse(html)

#==================================================================================
# Отчет о количестве(%) книг в электронном каталоге и в ЦБС + разрез по бибилотекам
@staff_member_required
def elcat_adm_report_books(request):
    # счетчик всех книг из таблицы elcat_book
    adm_report_books = connection.cursor()
    adm_report_books.execute(
        """
        SELECT COUNT(*) FROM  elcat_book
        WHERE 1=1
        ;
        """
    )

    # Внимание! Присутсвует
    # выборка значения, где указанно общее число всех книг в ЦБС
    # для этого из таблицы bookstotal  находим последний id и выбираем
    # соотвествущее ему значение из поля booksfromok
    # полученное число не забываем сделать вещественным
    books_total = bookstotal.objects.latest('id').booksfromok
    books_in_table = adm_report_books.fetchone()
    books_in_table = books_in_table[0]
    book_percent = round((( books_in_table / float(books_total)) * 100), 2)

    # запрос на выборку всех библиотек и книг в них
    # + расчет доли фонда каждой библиотеки в БД (процентах от суммарного количества)
    adm_report_books.execute(
        """
        SELECT   li.name  AS LibraryName
                ,COUNT(*) AS BooksCount
                ,li.library_id
        FROM     elcat_book b
                ,elcat_library li
        WHERE    li.Library_id = b.Library_id
        GROUP BY b.Library_id
        ;
        """
    )
    books_in_libraryes = adm_report_books.fetchall()
    books_in_libraryes_count = []
    for x,y,z in books_in_libraryes:
       try:
           w = booksatlibrary.objects.get(library_id=z).booksfromok
       except booksatlibrary.DoesNotExist:
           w = 0
           list1 = [ x, y, z, w ]
           books_in_libraryes_count.append( tuple(list1) )
           continue
       else:
           w = round(((y / float(w)) * 100), 2)
           list1 = [ x, y, z, w ]
           books_in_libraryes_count.append( tuple(list1) )
    books_in_libraryes_count = tuple(books_in_libraryes_count)

    # формирование шаблона
    templ = get_template('admin/AdmElcatReport.html')
    html = templ.render(Context({'books_in_table' : books_in_table,
                                 'book_percent': book_percent,
                                 'books_in_libraryes': books_in_libraryes,      # лишнее
                                 'books_in_libraryes_count': books_in_libraryes_count,
                                 'books_total' : books_total,
                                 'user': request.user
                                }))
    return HttpResponse(html)
