from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'site1/home.html')
def introduction(request):
    return render(request, 'site1/introduction.html')
