# coding=utf-8
from django.db import models

# Таблица с книгами Белоярской ЦБС --------------------------------
class book(models.Model):
#    BookCount_id = models.AutoField(primary_key=True)
    book_id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=512)
    inventory = models.IntegerField(null=True)
    volume = models.CharField(max_length=50,null=True)
    author_id = models.ManyToManyField('author')
    bookauthor_id = models.BigIntegerField()
    isbn = models.CharField(max_length=20,null=True)
    isbn10 = models.CharField(max_length=20,null=True)
    bbk1 = models.ForeignKey('bbk1')
    bbk2 = models.ForeignKey('bbk2')
    genre = models.ForeignKey('genre')
    series = models.ForeignKey('series')
    content = models.ForeignKey('content')
    publisher = models.ForeignKey('publisher')
    year = models.IntegerField()
    pages = models.IntegerField()
    language = models.ForeignKey('language')
    price = models.FloatField()
    shelfplace = models.ForeignKey('shelfplace')
    library = models.ForeignKey('library')
    librarytown = models.ForeignKey('librarytown')

    def __unicode__(self):
#       return unicode(self.Name, self.Library)
        return u'%s | %s | %s' % (self.name, self.library, self.librarytown)

#Таблица с авторами -----------------------------------------------
class author(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    author_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __unicode__(self):
       return unicode(self.name)

#Таблица с ББК1 ---------------------------------------------------
class bbk1(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    bbk1_id = models.BigIntegerField(primary_key=True)
    code1 = models.CharField(max_length=30)
    description1 = models.CharField(max_length=300)

    def __unicode__(self):
       return u'%s | %s' % (self.code1, self.description1)

#    def __unicode__(self):
#       return unicode(self.Description1)

#Таблица с ББК2 ---------------------------------------------------
class bbk2(models.Model):
    bbk2_id = models.BigIntegerField(primary_key=True)
    code2 = models.CharField(max_length=30)
    description2 = models.CharField(max_length=300)

    def __unicode__(self):
       return u'%s | %s' % (self.code2, self.description2)

#Таблица жанров ---------------------------------------------------
class genre(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    genre_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __unicode__(self):
       return unicode(self.name)

#Таблица серий книг -----------------------------------------------
class series(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    series_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __unicode__(self):
       return unicode(self.name)

#Таблица контента -------------------------------------------------
class content(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    content_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __unicode__(self):
       return unicode(self.name)

#Таблица издательств ----------------------------------------------
class publisher(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    publisher_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=512)
    city = models.CharField(max_length=200)

    def __unicode__(self):
       return unicode(self.name)

#Таблица языков книг ----------------------------------------------
class language(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    language_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __unicode__(self):
       return unicode(self.name)

#Таблица мест на полках -------------------------------------------
class shelfplace(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    shelfplace_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __unicode__(self):
       return unicode(self.name)

#Таблица библиотек ------------------------------------------------
class library(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    library_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __unicode__(self):
       return unicode(self.name)

#Таблица населенных пунктов где расположены библиотеки ------------
class librarytown(models.Model):
#    Count_id = models.AutoField(primary_key=True)
    librarytown_id = models.BigIntegerField(primary_key=True)
    town = models.CharField(max_length=200)

    def __unicode__(self):
       return unicode(self.town)

# Таблица с общим количеством книг из отдела комплектования
class bookstotal(models.Model):
    booksfromok = models.IntegerField()
    date = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return u'Количество книг на: %s' % (self.date)

# Таблица с количеством книг по библиотекам
class booksatlibrary(models.Model):
    library = models.ForeignKey('library')
    booksfromok = models.IntegerField()
    date = models.DateTimeField(auto_now=True, auto_now_add=True)

#    def __unicode__(self):
#        return u'Количество книг в: %s' % (library.library_id)