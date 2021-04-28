from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name_var_index = "Max Macavilca"
    return render(request, "base.html", {"template_name": name_var_index})
#    name = request.GET.get("varName") or "Empty"
#    return HttpResponse("Hello, {}!".format(name))

def search(request):
    search_string = request.GET.get("s") or "Please add a value"
    return HttpResponse("<h1>User searched for this keyword: {}</h1>".format(search_string))
