from django.contrib import admin
from .models import Event, Artist
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display  = ('title','date','city')
    list_filter = ('title','date','city')
    prepopulated_fields = {'slug': ('title',)}


class ArtistAdmin(admin.ModelAdmin):
    list_display  = ('name','genre')
    list_filter = ('name','genre')
    


admin.site.register(Event, EventAdmin)
admin.site.register(Artist, ArtistAdmin)