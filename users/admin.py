from django.contrib import admin
from .models import Personne,Patient,Docteur,Analyste,Pharmacien,Radiologue,Dossier
# Register your models here.
admin.site.register(Patient)
admin.site.register(Docteur)
admin.site.register(Analyste)
admin.site.register(Pharmacien)
admin.site.register(Radiologue)

