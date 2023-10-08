from django.db import models

class Kandidat(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    ime = models.TextField(max_length=256)
    brglasova = models.IntegerField()


class Glas(models.Model):
    id = models.IntegerField(primary_key=True)
    glasao = models.BooleanField()