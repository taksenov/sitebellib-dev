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
      AND b.Book_id        = 15708340906138
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
;