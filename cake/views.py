from django.shortcuts import render


def main_page(request):
    return render(request, "index.html")


def account(request):
    return render(request, "lk.html")
