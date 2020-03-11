from django.shortcuts import render

# Create your views here.

def Sample(request):
    return render(request, 'core/sample.html')