from django.contrib import admin
from user.models import Enseignant, Etudiant, CustomUser


admin.site.register(Enseignant)
admin.site.register(Etudiant)
admin.site.register(CustomUser)
