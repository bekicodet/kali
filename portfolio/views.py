from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def index(request):
    context = {
        'portfolios': Portfolio.objects.all()
    }
    return render(request, 'portfolio/index.html', context)

def about(request):
    context = {
        'abouts': Portfolio.objects.all()
    }
    return render(request, 'portfolio/about.html', context)

def work(request):
    context = {
        'works': Portfolio.objects.all()
    }
    return render(request, 'portfolio/work.html', context)

def contact(request):
    context = {
        'contact': Portfolio.objects.all()
    }
    return render(request, 'portfolio/contact.html', context)