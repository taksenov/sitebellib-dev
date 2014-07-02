 select 
b.*
,li.name
      ,li.Library_id 
      
      ,lt.town AS LibraryTown
      ,lt.LibraryTown_id

FROM   elcat_book b
      ,elcat_library li
      ,elcat_librarytown lt
WHERE  li.Library_id = b.Library_id
and       lt.librarytown_id = b.librarytown_id
and b.Library_id not in
(
18502950989215,              #Центральная
10521961277166,              #Детская
18172310046123,              #юношеская
13575720298187,              #казым
26258710197167,              #лыхма
850957612410219,              #верхнеказымский
45632751167163,              #сорум
11331140778190,              #сосновка
11762410167164,              #полноват
942272203010220              #ванзеват
)
;