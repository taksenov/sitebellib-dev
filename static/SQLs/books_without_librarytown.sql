SELECT   e.name
        ,e.librarytown_id
        ,lt.town as LibraryTown
        ,e.library_id
        ,lib.name as LibraryName
FROM  elcat_book        e
     ,elcat_librarytown lt
     ,elcat_library     lib
where 1=1
and e.librarytown_id not in
(
280820130000001,
280820130000002,
280820130000003,
280820130000004,
280820130000005,
280820130000006,
280820130000007,
280820130000008
)
and e.librarytown_id = lt.librarytown_id
and e.library_id = lib.library_id
;