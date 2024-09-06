from django.contrib import admin
from . models import Game,offer

class GamesAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
    
class offerAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(Game,GamesAdmin)
admin.site.register(offer,offerAdmin)