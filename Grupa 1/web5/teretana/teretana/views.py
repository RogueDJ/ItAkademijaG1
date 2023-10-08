from django.shortcuts import render
from teretana.models import Program, Vezba

def vezbe(req):
    programi_vezbi = Program.objects.all()

    id_programa = int(req.GET.get("program")) if req.GET.get("program") else 0

    vezbe = Vezba.objects.filter(program = id_programa)

    izlaz = render(req,"index.html",{
        'programi':programi_vezbi,
        "vezbe": vezbe,
        "idprograma":id_programa
        })
    return izlaz