# coding: utf-8

# Шаблонный тег для вывода текущего года на всех страницах сайта
# чтобы можно было менять год в одном месте (в БД таблица = site_year),
# а не на всех страницах сайта по отдельности.

from django.db import connection
from django.template.base import Library, Node

register = Library()

class SiteYearNode(Node):
    def render(self, context):
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
        return year_result[0]

def siteyear_tag(parser, token):
    return SiteYearNode()

siteyear_tag = register.tag(siteyear_tag)