from email import message
from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message_type', 'message']

        # widgets = {"name": forms.TextInput(
        #     attrs={"form_control valid"}),  "message": forms.Textarea(attrs={"class": "form_control valid"}), }
        MT = (
            ('Общие вопросы', 'Общие вопросы'),
            ('Претензии|Жалобы|Замечания к работе',
             'Претензии|Жалобы|Замечания к работе'),
            ('Диспетчерская служба', 'Диспетчерская служба'),
            ('Тепловая инспекция', 'Тепловая инспекция'),
        )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': "form_control valid"}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail',
                                            'cols': 30,
                                            'rows': 9,
                                            'class': "form_control valid"}),
            'message_type': forms.Select(attrs={'class': "form_control valid"}),
            'message': forms.Textarea(attrs={'placeholder': 'Введите текст собщения', 'cols': 30, 'rows': 9, 'class': "form_control valid"}),
        }
