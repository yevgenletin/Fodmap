from django.db import models
# Create your models here.

class Servivio(models.Model):
    name = models.CharField(max_length= 50)
    fructosa = models.CharField(max_length= 50)
    lactosa = models.CharField(max_length= 50)
    sorbitol = models.CharField(max_length= 50)
    gos = models.CharField(max_length= 50)
    fructano = models.CharField(max_length= 50)
    gr = models.CharField(max_length= 50)
    comment = models.CharField(max_length= 50)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.name




