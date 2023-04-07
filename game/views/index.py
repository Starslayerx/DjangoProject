from django.shortcuts import render


def index(requet):
    return render(request, "multiends/web.html")
