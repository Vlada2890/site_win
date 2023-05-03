from django.shortcuts import render


def home(request):
    return render(request, "main/home.html")


def types(request):
    return render(request, "main/types.html")


def grown(request):
    return render(request, "main/grown.html")


def food(request):
    return render(request, "main/food.html")