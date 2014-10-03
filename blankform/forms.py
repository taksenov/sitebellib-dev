__author__ = 'taksenov'
# coding=utf-8

from django import forms

ANSWER_CHOICES = (
                  (1, 'Удовлетворен'),
                  (2, 'Частично удовлетворен'),
                  (3, 'Не удовлетворен')
                 )

class blank_form(forms.Form):
    answer1 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer2 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer3 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer4 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer5 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer6 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer7 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer8 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer9 =  forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer10 = forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer11 = forms.ChoiceField(required=True, choices=ANSWER_CHOICES)
    answer12 = forms.ChoiceField(required=True, choices=ANSWER_CHOICES)












