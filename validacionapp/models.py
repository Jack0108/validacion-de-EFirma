from django.db import models

# Create your models here.

class archivo(models.Model):
    archivo= models.FileField()
    
    class Meta:
        verbose_name_plural="archivos"

def __str__(self):
    return self.archivo.name
