from django.shortcuts import render, HttpResponse


# Create your views here.
def blog_home(request):
    return render(request, 'blog.html')


def index_home(request):
    return render(request, 'index.html')


def about_home(request):
    return render(request, 'about.html')


def contact_home(request):
    return render(request, 'contact.html')


def portfolio_home(request):
    return render(request, 'portfolio.html')