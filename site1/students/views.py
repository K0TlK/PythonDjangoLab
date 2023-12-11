from django.shortcuts import render


def index(request):
    return render(request, "students/index.html")


def info(request):
    return render(request, "students/info.html")
