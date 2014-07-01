SELECT qdlist_name.NameDocumentFull
            ,qdlist_quantizeddoc.QDDate
            ,qdlist_quantizeddoc.QDNumSerial
            ,qdlist_quantizeddoc.QDNumFromPublication
            ,qdlist_links.DomainLinkName
            ,qdlist_name.NameDocument
            ,qdlist_quantizeddoc.QDNumExtra
        FROM qdlist_quantizeddoc
            ,qdlist_links
            ,qdlist_Name
            ,qdlist_years
        WHERE 1=1
            AND qdlist_years.year_id = %s
            AND qdlist_quantizeddoc.year_id = qdlist_years.year_id
            AND qdlist_quantizeddoc.name_id = qdlist_name.name_id
            AND qdlist_quantizeddoc.link_id = qdlist_links.link_id
        ORDER BY (qdlist_quantizeddoc.QDNumSerial + 0)