from django.contrib import admin
from . models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
     list_display = ('image_tag','title')
     search_fields = ('title',)
     list_filter = ('cat',)

admin.site.register(Post, PostAdmin)
