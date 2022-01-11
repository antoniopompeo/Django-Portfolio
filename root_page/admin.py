from django.contrib import admin
from .models import Project #para que tome los datos de la clase que cree
 
admin.site.register(Project) #que aparezca la opcion de registrar un nuevo Project en la seccion admin de la pagina 


