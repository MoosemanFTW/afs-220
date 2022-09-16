from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def bellagio(request):
    return render(request, 'pages/bellagio.html')

def stratosphere(request):
    return render(request, 'pages/stratosphere.html')

def freemont(request):
    return render(request, 'pages/freemont.html')