from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name__name=menu_name)
    return {'menu_items': menu_items}

