"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account import views as allauth_views
from allauth.socialaccount.providers.vk.views import oauth2_callback, oauth2_login
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from firstapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", allauth_views.login, name="account_login"),
    path("login/vk/", oauth2_login, name="vk_login"),
    re_path(r"^login/vk/callback/$", oauth2_callback, name="vk_callback"),
    path("signup/", views.signup, name="account_signup"),
    path("logout/", views.logout_view, name="account_logout"),
    path("about/", TemplateView.as_view(template_name="firstapp/about.html")),
    path("", views.index, name="order_create"),
    path("orders/", views.orders_list, name="order_list"),
    path("orders/<int:order_id>/", views.order_detail, name="order_detail"),
]

urlpatterns += [path("social/", include("allauth.socialaccount.urls"))]
