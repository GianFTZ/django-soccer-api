from django.contrib import admin
from sports.models import Local

class Locals(admin.ModelAdmin):
    list_display = ('id', 'nome', 'price' )
    list_display_links = ('id', 'nome', 'price')
    search_fields = ('nome',)

admin.site.register(Local, Locals)