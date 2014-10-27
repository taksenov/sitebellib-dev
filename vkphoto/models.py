__author__ = 'taksenov'
#coding: utf-8

from django.db import models

# Таблица с фотогалереями(новостями) из вконтакта
class vknews(models.Model):
    news_text = models.CharField(max_length=5000)
    datetime = models.DateTimeField(auto_now=True, null=True)

