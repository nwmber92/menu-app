from django.contrib import admin
from menu.models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(MenuItem)
admin.site.register(Menu, MenuAdmin)


