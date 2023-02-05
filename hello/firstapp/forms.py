from django import forms
from django.forms import BaseFormSet
from firstapp.models import OrderItem


class OrderItemForm(forms.ModelForm):
    article = forms.CharField(
        max_length=20,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Артикул"}),
    )
    quantity = forms.IntegerField(
        max_value=50,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Количество"}),
    )
    size = forms.CharField(
        max_length=5,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Размер"}),
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Цена"}),
    )

    class Meta:
        model = OrderItem
        exclude = ["order", "id"]


class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False
            form.use_required_attribute = True


OrderItemFormset = forms.formset_factory(
    OrderItemForm, extra=1, formset=RequiredFormSet
)
