from django.shortcuts import render
from django.contrib.auth import authenticate, login as lgn
from django.http import HttpResponseRedirect
from glasanje.models import Kandidat, Glas
def loginforma(req):
    return render(req, "login.html")

def login(req):
    uname = req.POST.get("username")
    passwd = req.POST.get("password")
    user = authenticate(username=uname,password=passwd)
    if user:
        lgn(req,user)
        return HttpResponseRedirect('/kandidati')
    else:
        return HttpResponseRedirect('/loginforma')
        

def kandidati(req):
    korisnik = req.user
    if not korisnik.is_authenticated:
        return HttpResponseRedirect('/loginforma')
    
    
    svi_kandidati = Kandidat.objects.all()
    return render(req,"kandidati.html",{"kandidati":svi_kandidati})

def glasanje(req):
    korisnik = req.user
    if not korisnik.is_authenticated:
        return HttpResponseRedirect('/loginforma')
    
    id_kandidata = int(req.GET.get("id"))
    id_korisnika = korisnik.id
    glasao = False
    try:
        glasao = Glas.objects.get(id=id_korisnika)
    except:
        pass
    poruka = ""
    if glasao:
        poruka = "Ne mozes da glasas ponovo"
    else:
        glas = Glas()
        glas.id = id_korisnika
        glas.glasao = True
        glas.save()
        kandidat = Kandidat.objects.get(id=id_kandidata)
        kandidat.brglasova+=1
        kandidat.save()
        poruka = "Uspesno si glasao"
    return render(req,"glasanje.html",{"poruka":poruka})

