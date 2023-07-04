from django.contrib import admin
from .models import Character, House

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')