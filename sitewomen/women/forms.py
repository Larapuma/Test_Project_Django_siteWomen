from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, BaseValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband

@deconstructible
class RussianValidator:
    ALLOWED_CHARS ="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"+"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower()+"0123456789- "
    code = "russian"

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."

    def __call__(self,value, *args, **kwargs):
        if not (set(value)<=set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message,code = self.code)


class AddPostForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=255, label="Заголовок"
                            , widget=forms.TextInput(attrs={'class': 'form-input'}),

    error_messages={
            'min_length':"Слишком короткий заголовок",
            'required':"Без заголовка никак",
        })
    slug = forms.SlugField(max_length=255, label="URL",
                           validators=[
                               MinLengthValidator(5,message='минимум 5 символов'),
                               MaxLengthValidator(100,message='максимум 100 символов'),
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label="Контент")
    is_published = forms.BooleanField(required=False, label="Статус")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="Категория не выбрана", label="Категории")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),empty_label="Не замужем", required=True, label="Муж")

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower() + "0123456789- "
        if not (set(title)<=set(ALLOWED_CHARS)):
            raise ValidationError("Должны присутствовать только русские символы, дефис и пробел.")