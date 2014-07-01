# coding=utf-8
__author__ = 'taksenov'

from django.db import connection
last_year = connection.cursor()
last_year.execute("""
    SELECT sy.year
    FROM   site_year sy
    WHERE  sy.id = (
                    SELECT MAX(sy.id)
                    FROM   site_year sy
                   )
    ;
    """)                    # Запрос вернет год с максимальным айдишником,
                            # а так как текущий год добавляется в таблицу ручками,
                            # то и айдишник у этого года будет максимальный,
                            # т.к. id это автоинкрементное поле
year_result = last_year.fetchone()
print year_result
