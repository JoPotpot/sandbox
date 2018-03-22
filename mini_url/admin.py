from django.contrib import admin
from .models import MiniUrl

class MiniUrlAdmin(admin.ModelAdmin):
    list_display = ('URL_longue', 'code', 'date', 'createur', 'count')
    list_filter = ('createur', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('URL_longue', )

admin.site.register(MiniUrl, MiniUrlAdmin)