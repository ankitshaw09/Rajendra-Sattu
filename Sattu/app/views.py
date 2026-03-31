from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'product.html')

def story(request):
    return render(request, 'story.html')


def contact(request):
    return render(request, 'contact.html')

def process(request):
    return render(request, 'ourProcess.html') 