# coding=utf-8
from django.db import models

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

#    class Meta:
#        ordering = ['QDNumSerial']                                            # Сортируем по порядковому номеру

# Таблица с названиями (торговыми марками) документов
class name(models.Model):
    Name_id = models.AutoField(primary_key=True)
    NameDocument = models.CharField(max_length=10)
    NameDocumentFull = models.CharField(max_length=256)

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

