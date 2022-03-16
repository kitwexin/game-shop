from django.shortcuts import render

def home_page(request):
    return render(request,'main/home_page.html')

def about_us(request):
    return render(request,'main/about.html')