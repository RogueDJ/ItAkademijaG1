from django.db.models import Model
from django.db import models

class Program(Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    naziv = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.naziv
    
class Vezba(Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    naziv = models.CharField(max_length=256)
    opis = models.CharField(max_length=14000)
    program = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id} {self.naziv}"
