from django.contrib import admin

# Register your models here.

from .models import Localizacao, Banda, Festival

admin.site.register(Localizacao)
admin.site.register(Banda)
admin.site.register(Festival)