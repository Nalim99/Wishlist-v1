from django.shortcuts import render
from .models import Item

def index(request):
    all_items = Item.objects.all()
    return render(request, 'overview/index.html', {'all_items': all_items})
