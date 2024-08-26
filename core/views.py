from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello, world!\nEu sou {nome} e tenho {idade} anos.</h1>')
