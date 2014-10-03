__author__ = 'taksenov'
# coding=utf-8

from django.db import models

# Таблица с вопросами -------------------------
class question(models.Model):
    question_id = models.IntegerField(primary_key=True, unique=True)
    question = models.CharField(max_length=512)
    # answer = models.ForeignKey('answer')
    isdeleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
       return unicode(self.question)

# Таблица с вариантами ответов ----------------
class answer(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=30)
    isdeleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
       return unicode(self.answer)

# таблица с ответами клиентов -----------------
class clientsanswers(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    client_id = models.ForeignKey('clientsession')
    question_id = models.ForeignKey('question')
    answer_id = models.ForeignKey('answer')
    datetime = models.DateTimeField(auto_now=True, null=True)

# таблица с сессиями клиентов -----------------
class clientsession(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    clientsession = models.CharField(max_length=90)
    customcomment = models.CharField(max_length=1024, null=True)
    datetime = models.DateTimeField(auto_now=True, null=True)