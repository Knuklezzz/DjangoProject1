from django.contrib.auth import logout
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404, render

from .forms import OrderItemFormset
from .models import Order, OrderItem


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    formset = OrderItemFormset(request.POST or None, prefix="form")
    if request.method == "POST":
        if formset.is_valid():
            order = Order.objects.create(user=request.user)
            for form in formset:
                print(form)
                if form.is_valid():
                    OrderItem.objects.create(order=order, **form.cleaned_data)
                else:
                    return render(request, "firstapp/index.html", {"formset": formset})
            order.calculate_total_price()
            return render(
                request, "firstapp/index.html", {"formset": OrderItemFormset()}
            )

    return render(request, "firstapp/index.html", {"formset": formset})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def signup(request):
    return HttpResponseRedirect("/login/")


def success_login(request):
    return HttpResponseRedirect("/")


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def orders_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    orders = Order.objects.filter(user=request.user)
    return render(
        request,
        "firstapp/orders_list.html",
        {"orders": orders, "orders_sum": sum([order.total_price for order in orders])},
    )


def order_detail(request, order_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "firstapp/order_detail.html", {"order": order})
