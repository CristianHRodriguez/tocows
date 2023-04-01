from django.db import models
from datetime import date

# Create your models here.
class Cows(models.Model):
    numberC=models.IntegerField()
    nameC=models.CharField(max_length=45)
    breedC=models.CharField(max_length=45) #raza
    momC=models.IntegerField()
    dadC=models.IntegerField()
    sex=models.CharField(max_length=1) #M o H
    realBorn=models.DateField(default=date.today)
    activo=models.BooleanField(default=True)
    #campos adicionales: edad, numero partos
    
class BornCows(models.Model):
    id_cowB=models.ForeignKey(Cows, on_delete=models.CASCADE, db_column='numCowB',related_name="numVacasB")
    dateMonta = models.DateField(default=date.today) #ultimo_servicio
    id_son=models.IntegerField(blank=True, null=True) #num_hijo
    pregnant=models.BooleanField(default=True, null=True) #quedo o no embarazada
    #campos adicionales: proxCalor, fechaParto

class photo(models.Model):
    id_cowP=models.ForeignKey(Cows, on_delete=models.CASCADE, db_column='numCowP', related_name="numVacasP")
    photo=models.TextField()
    def __str__(self):
        return self.photo