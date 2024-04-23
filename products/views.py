from django.shortcuts import render
from .models import Product

def all_wines(request):
    """A view to show all wines and allow sorting and searching """

    wines = Product.objects.all()

    context = {
        'wines': wines,
    }

    return render(request, 'products/wines.html', context)
