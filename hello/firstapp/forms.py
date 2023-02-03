from django import forms

class UserForm(forms.Form):
    article = forms.CharField(label = "Артикул", max_length=20)
    size = forms.CharField(label = "Размер", max_length=20)
    clrChoise = (1, "Бриллиантовый"), (2, "Черный"), (3, "95 (Серый)")
    btnClr = forms.ChoiceField(label="Цвет кнопки",choices=clrChoise)
    amount = forms.IntegerField(label="Количество")
    ad = forms.BooleanField(label="Я согласен получать рассылку в Telegram", required=False)
