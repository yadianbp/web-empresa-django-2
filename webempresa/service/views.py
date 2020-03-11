from django.shortcuts import render,HttpResponse
from .models import Service
# Create your views here.

def Services(request):
    services = Service.objects.all()
    return render(request, 'service/services.html', {'services':services})