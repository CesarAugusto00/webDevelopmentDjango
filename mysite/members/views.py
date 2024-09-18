from django.shortcuts import render

# Create your views here.
def ej1(request):
    #request get 3 arguments. a request, a template as second and dictionary as third
    return render(request, "members/contextual.html")

def second(request):
    return render(request, "members/hh.html")