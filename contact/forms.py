from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("email", "name", "firstname", "phone", "text", "soglasen", "status", "image")
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Ваш Email..."}),
            "name": forms.TextInput(attrs={"class": "editContent", "placeholder": "Ваше имя..."}),
            "firstname": forms.TextInput(attrs={"class": "editContent", "placeholder": "Ваша фамилия..."}),
            "text": forms.Textarea(attrs={"class": "editContent", "placeholder": "Ваше обращение ..."}),
            "phone": forms.TextInput(attrs={"class": "editContent", "placeholder": "Ваш телефон..."}),
            "soglasen": forms.CheckboxInput(attrs={"class": "editContent", "before": "согласен..."}),
            "image": forms.FileInput(attrs={"class": "editContent", "before": "согласен..."}),

        }
        labels = {
            "email": '',
            "name": '',
            "firstname": '',
            "phone": '',
            "text": '',
            "file_obj": '',
            "soglasen": 'согласен',
            "status": 'выберите',
        }
