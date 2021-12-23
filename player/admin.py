from django.contrib import admin
from .models import T20Players, ODIPlayers, TestPlayers
# Register your models here.


admin.site.register(T20Players)
admin.site.register(ODIPlayers)
admin.site.register(TestPlayers)
