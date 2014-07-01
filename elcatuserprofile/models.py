# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# in models.py:
from django.db.models import signals
from elcatuserprofile.signals import create_profile


# When model instance is saved, trigger creation of corresponding profile
signals.post_save.connect(create_profile, sender=User)

# Create your models here.
class chb(models.Model):
    # поле для связки со встроенной моделью пользователя Django
    user = models.ForeignKey(User, unique=True)
    # новые поля для данных о читательском билете
    # суффикс _chb -- имеет отношение к читательскому билету
    # суффикс _user -- имеет отношение к пользователю
    number_chb = models.IntegerField(blank=True, null=True)
    year_chb = models.IntegerField(blank=True, null=True)
    sur_name_user = models.CharField(max_length=200, blank=True, null=True)
    year_user = models.IntegerField(blank=True, null=True)
    phone_user = PhoneNumberField(null=True, blank=True)
    # номер электронного читательского билета
    num_electro_chb = models.CharField(max_length=200, blank=True, null=True)