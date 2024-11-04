from django.contrib import admin
from conciertoApp.models import Entrada, Persona, Concierto

admin.site.register(Entrada,Persona,Concierto)
