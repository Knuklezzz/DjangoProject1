from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import UserForm

def index(request):
    form = UserForm()
    if request.method == "POST":
        #name = request.POST.get("name")
        #age = request.POST.get("age")
        form = UserForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data['article']
            output = "<h2>Позиция 1</h2><h3>Артикул - {0}</h3>".format(article)
            return HttpResponse(output)

    return render(request, "firstapp/index.html", {"form": form})

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>User</h2><h3>id: {0} Name: {1}</h3>".format(id,name)
    return HttpResponse(output)

# Create your views here.