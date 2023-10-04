from django.urls import resolve
from menu.models import MenuItem


def menu_processor(request):
    current_url = resolve(request.path_info).url_name
    MenuItem.objects.update(active=False)
    active_items = MenuItem.objects.filter(url=current_url)
    for item in active_items:
        item.active = True
        item.save()
        parent = item.parent
        while parent is not None:
            parent.active = True
            parent.save()
            parent = parent.parent

    return {}
