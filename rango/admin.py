from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']
    search_fields = ['title']
    list_filter = ['views']


class PageInline(admin.TabularInline):
    model = Page
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'likes']
    list_filter = ['views', 'likes']

    inlines = [PageInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
