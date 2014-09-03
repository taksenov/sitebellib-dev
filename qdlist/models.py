# coding=utf-8
from django.db import models

# таблица с Категориями оцифрованного контента
# (Периодика, Собственные издания и т.д.)
class type(models.Model):
    type_id = models.AutoField(primary_key=True)
    typename = models.CharField(max_length=30, null=False)

    def __unicode__(self):
        return u'Тип оцифрованных документов: %s (ID=%s)' % (self.typename, self.type_id)

# таблица с подкатегориями документов
# у одной категрии может быть много подкатегорий, но не наоборот
# связь один ко многим
class subtype(models.Model):
    subtype_id = models.AutoField(primary_key=True)
    subtypename = models.CharField(max_length=25, null=False)
    subtypedescription = models.CharField(max_length=25, null=False)
    type = models.ForeignKey('type', null=True)
    linktypename = models.CharField(max_length=1, null=False, default='s')

    def __unicode__(self):
        return self.subtypename

# Таблица со списком оцифрованных документов
class quantizeddoc(models.Model):
    QuantizedDoc_id = models.AutoField(primary_key=True)
    Name = models.ForeignKey('name',null=True)                                # Name_id
    Year = models.ForeignKey('years')                                         # Year_id
    QDNumSerial = models.CharField(max_length=11,null=True)
    QDNumFromPublication = models.CharField(max_length=11,null=True)
    QDDate = models.DateField(null=True)
    QDNumExtra = models.CharField(max_length=11,null=True)
    Link = models.ForeignKey('links',null=True)                               # Link_id

    def __unicode__(self):
        return self.Name.NameDocumentFull

#    class Meta:
#        ordering = ['QDNumSerial']                                            # Сортируем по порядковому номеру

# Таблица с названиями (торговыми марками) документов
class name(models.Model):
    Name_id = models.AutoField(primary_key=True)
    NameDocument = models.CharField(max_length=64)
    NameDocumentFull = models.CharField(max_length=400)
    subtype = models.ForeignKey('subtype',null=True)

    def __unicode__(self):
        return self.NameDocumentFull

    def __unicode__(self):
        return self.NameDocument

# Таблица годов изданий
class years(models.Model):
    Year_id = models.IntegerField(unique=True, primary_key=True)
    YearName = models.IntegerField()

    def __unicode__(self):
        return unicode(self.YearName)

# Таблица с ссылкой на домены внутри кторых лежат документы (на облачное хранилище selectel)
class links(models.Model):
    Link_id = models.AutoField(primary_key=True)
    DomainLinkName = models.URLField()

    def __unicode__(self):
        return unicode(self.DomainLinkName)
