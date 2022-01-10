from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

#las clases que voy a necesitar para almacenar los datos en la base de datos

class Project(models.Model):
    title = CharField(max_length=40)
    description = CharField(max_length=200)
    image = ImageField(upload_to = "root_page/images/")  #lo va a guardar root_page/images pero en una carpeta llamada media porque es lo que setee en el archivo settings.py 
    url_github = URLField(blank = True)
    url_colab = URLField(blank = True)