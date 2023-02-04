from django import forms
from firstapp.models import OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ["order", "id"]


OrderItemFormset = forms.formset_factory(OrderItemForm, extra=1)
