from django.contrib import admin
from django.utils.html import format_html
from .models import Banda
from .models import Album
from .models import Musica
# Register your models here.



admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Musica)
