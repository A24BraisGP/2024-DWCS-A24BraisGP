from django.contrib import admin
from .models import Event,Game
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','city','date')
    list_filter = ('title','city','date')
    
class GameAdmin(admin.ModelAdmin):
    list_display = ('title','recommended_age')
    list_filter = ('title', 'recommended_age')
admin.site.register(Event,EventAdmin)
admin.site.register(Game,GameAdmin)