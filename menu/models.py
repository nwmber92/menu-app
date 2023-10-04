from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    menu_name = models.ForeignKey(Menu, blank=True, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.url:
            return reverse(self.url)
        return '#'
