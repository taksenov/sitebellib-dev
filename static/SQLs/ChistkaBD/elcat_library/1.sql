# поиск id библиотек
SELECT
e.*
#e.Library_id
FROM elcat_library e
where 1=1

#and e.Library_id <> 11762410167164
/*
and e.Library_id not in
(
18502950989215,              #Центральная                   1
10521961277166,              #Детская
18172310046123,              #юношеская
13575720298187,              #казым                         1
26258710197167,              #лыхма
850957612410219,              #верхнеказымский              1
45632751167163,              #сорум
11331140778190,              #сосновка
11762410167164,              #полноват
942272203010220              #ванзеват
)



and e.name like '%по%'
and e.name not like '%оват%'
and e.name not like '%лно%'
and  e.name not like '%полн%'

and e.name like '%КСМО%'
and e.name not like '%алг%'
and e.name not like '%ама%'
and e.name not like '%изо%'
and e.name not like '%оли%'
and e.name not like '%фан%'
and e.name not like '%слово%'
and e.name not like '%дом%'
and e.name not like '%бар%'
and e.name not like '%terr%'
and e.name not like '%бра%'
and e.name not like '%ком%'
and e.name not like '%сов%'
and e.name not like '%яуз%'
and e.name not like '%мид%'
and e.name not like '%вал%'
and e.publisher_id <> 73915261429211

and e.name not like '%харв%'
and e.name not like '%ли%'
and e.name not like '%ма%'
and e.name not like '%час%'
and e.publisher_id <> 73915261429211

and e.publisher_id <> 40362230519213

and e.name not like '%алго%'
and e.name not like '%яуза%'
and e.name not like '%амаль%'
and e.name not like '%комм%'
and e.name not like '%изогра%'
and e.name not like '%олимп%'
and e.name not like '%олис%'
and e.name not like '%слов%'
and e.name not like '%фантом%'
and e.name not like '%домино%'
and e.name not like '%барба%'
and e.name not like '%Zeб%'
and e.name not like '%mar%'
and e.name not like '%terr%'
and e.name not like '%мидг%'
and e.name not like '%Носов%'
and e.name not like '%валери%'
and e.name not like '%марк%'
and e.name not like '%сова%'
and e.name not like '%экспрес%'
*/
order by e.name

;