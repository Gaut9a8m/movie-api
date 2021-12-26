from django.contrib import admin
from .models import HollywoodMovie, BollywoodMovie
# Register your models here.
class HollywoodMovieAdmin(admin.ModelAdmin):
    list_display = ['pk','title','release_date','created_on']

admin.site.register(HollywoodMovie, HollywoodMovieAdmin)
admin.site.register(BollywoodMovie)
