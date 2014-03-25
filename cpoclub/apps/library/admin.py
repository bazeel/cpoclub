from django.contrib import admin
from library.models import Doc, Category


class DocAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'category']
    list_editable = ['active']
    search_fields = ['title', 'category']


admin.site.register(Category)
admin.site.register(Doc, DocAdmin)