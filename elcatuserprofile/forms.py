# coding=utf-8
import django
from django import forms
from django.db import models
from elcatuserprofile.models import chb
from django.forms import ModelForm


class ProfileForm(django.forms.ModelForm):
    first_name = django.forms.CharField(max_length=30, required=False)
    last_name = django.forms.CharField(max_length=30, required=False)

    def __init__(self, *args, **kwargs):
        # получаем обьект профайла
        self.prof = kwargs.get('instance', None)
        initial = {
            'first_name': self.prof.user.first_name,
            'last_name': self.prof.user.last_name

        }
        # в два поля нашей формы помещаем значения соотв.полей из модели user
        kwargs['initial'] = initial
        super(ProfileForm, self).__init__(*args, **kwargs)
        # русские названия полей1
        self.fields['last_name'].label = "Фамилия"
        self.fields['first_name'].label = "Имя"
        self.fields['sur_name_user'].label = "Отчество"
        self.fields['year_user'].label = "Год рождения"
        self.fields['phone_user'].label = "Телефон"
        self.fields['number_chb'].label = "Формуляр читателя. Номер"
        self.fields['year_chb'].label = "Формуляр читателя. Год"
        self.fields['num_electro_chb'].label = "Электронный читательский билет. UID"
        # поля доступные только для чтения
        self.fields['num_electro_chb'].widget.attrs['readonly'] = True
        self.fields['year_chb'].widget.attrs['readonly'] = True
        self.fields['number_chb'].widget.attrs['readonly'] = True
        self.fields['phone_user'].widget.attrs['readonly'] = True
        self.fields['year_user'].widget.attrs['readonly'] = True

    class Meta:
        # форма для нашей модели профайла
        # model = models.UserProfile
        model = chb
        # для красоты, чтобы поля в форме шли в правильном порядке
        fields = (
            'last_name',                # фамилия
            'first_name',               # Имя
            'sur_name_user',            # отчество
            'year_user',                # год рождения
            'phone_user',               # телефон
            'number_chb',               # Номер читательского билета
            'year_chb',                 # год читательского билета
            'num_electro_chb',          # электронный читательский билет

        )

    def save(self, commit=True):
        super(ProfileForm, self).save(commit)
        if commit:
            self.prof.user.first_name = self.cleaned_data['first_name']
            self.prof.user.last_name = self.cleaned_data['last_name']
            self.prof.user.save()

# from django import forms
# import profiles
# from django.db import models
# from django.forms import ModelForm
# from elcatuserprofile.models import chb
# from django.contrib.auth.models import User
# from django.forms.models import modelformset_factory, inlineformset_factory, formset_factory
#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']
#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = chb
#         fields = ['number_chb', 'year_chb', 'sur_name_user', 'year_user', 'phone_user']
#
# ProfileFormSet = inlineformset_factory(User, chb)
