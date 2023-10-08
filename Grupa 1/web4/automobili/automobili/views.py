from django.http import HttpResponse
from django.shortcuts import render

def proba(request):
    odgovor = render(request, "proba.html")
    return odgovor

def naslovnastrana(request):
    odgovor = render(request, "index.html", {
    "oglasi":[
    {"id":1,"naziv":"Lotus","slika":"","cena":100},
    {"id":3,"naziv":"Lamborgini","slika":"","cena":200},
    {"id":4,"naziv":"Tesla","slika":"","cena":300},
    {"id":7,"naziv":"Delorean","slika":"","cena":400},
    {"id":15,"naziv":"Yugo","slika":"","cena":500}
    ]})    
    return odgovor

def detalji(request):
    odgovor = HttpResponse("Pozdrav iz strane sa detaljima <a href = '/'> Idi nazad</a>")
    return odgovor
