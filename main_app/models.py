from email.policy import default

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Talaba(models.Model):
    ism=models.CharField(max_length=200)
    guruh=models.CharField(max_length=50,null=True,blank=True)
    kurs=models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    kitob_soni=models.PositiveSmallIntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    JINS=(
       ('Erkak','Erkak'),
       ('Ayol','Ayol'),
    )
    ism=models.CharField(max_length=200)
    jins=models.CharField(max_length=200,choices=JINS)
    t_sana=models.DateField(blank=True,null=True)
    kitob_soni=models.PositiveSmallIntegerField(blank=True,null=True)
    tirik=models.BooleanField(default=False)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom=models.CharField(max_length=200)
    janr=models.CharField(max_length=100)
    sahifa=models.PositiveSmallIntegerField()
    muallif=models.ForeignKey(Muallif,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.nom


class Kutubxonachi(models.Model):
    ism=models.CharField(max_length=200)
    ish_vaqti=models.TimeField(blank=True,null=True)

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba=models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE)
    kutubxon=models.ForeignKey(Kutubxonachi,on_delete=models.CASCADE)
    olingan_vaqt=models.DateTimeField(auto_now_add=True)
    qaytargan_vaqt=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.talaba.ism}--{self.kitob.nom}"

