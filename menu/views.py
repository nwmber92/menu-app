from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def first_lvl(request):
    return render(request, 'first_lvl.html')


def second_lvl(request):
    return render(request, 'second_lvl.html')


def third_lvl(request):
    return render(request, 'third_lvl.html')
