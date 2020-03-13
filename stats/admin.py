from django.contrib import admin
from .models import Company, Game, GamePlayer, Results

# Register your models here.
admin.site.register(Company)
admin.site.register(Game)
admin.site.register(GamePlayer)
admin.site.register(Results)