from django.shortcuts import render
from django.views.generic import View

def dashboard(request):

    return render(request, 'inventory/dashboard.html', {})
