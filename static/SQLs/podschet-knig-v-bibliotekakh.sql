SELECT li.name
      ,li.Library_id 
      ,COUNT(*) AS 'Кол-во книг'
      ,lt.town AS LibraryTown
      ,lt.LibraryTown_id
FROM   elcat_book b
      ,elcat_library li
      ,elcat_librarytown lt
WHERE  li.Library_id = b.Library_id
and       lt.librarytown_id = b.librarytown_id
#and       lt.LibraryTown_id = 96874110029208
GROUP BY b.Library_id
;


#Использование «GROUP BY» и «HAVING» на примере задачи: вывести названия городов, в которых больше одного клуба, и их количество.
#SELECT city_name, count(*) AS `Количество` FROM city GROUP BY city_name HAVING count(*)>1