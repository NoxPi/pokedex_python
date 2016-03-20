from django.contrib import admin

# Register your models here.
from .models import Pokemon
from .models import Type


class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'english_full_name', 'japanese_full_name']
    ordering = ['id']

    class Meta:
        model = Pokemon


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']

    class Meta:
        model = Type

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Type, TypeAdmin)
