from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    some_var = ["тест", "тест", "тест"]
    return render(request, 'myapp/first.html', {'ggg': some_var})



def about(request):
    return HttpResponse("About us")



