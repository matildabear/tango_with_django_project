from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
            fields = ('title', 'category', 'urls')

    
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
