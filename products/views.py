from django.shortcuts import render, get_object_or_404
from .models import Product

def all_wines(request):
    """A view to show all wines and allow sorting and searching """

    wines = Product.objects.all()

    context = {
        'wines': wines,
    }

    return render(request, 'products/wines.html', context)

def wine_detail(request, product_id):
    """A view to show product details """

    wine = get_object_or_404(Product, pk=product_id)

    context = {
        'wine': wine,
    }

    return render(request, 'products/wine_detail.html', context)