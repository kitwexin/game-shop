from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def about_us(request):
    return render(request, 'about.html')