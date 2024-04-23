from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

def all_wines(request):
    """A view to show all wines and allow sorting and searching """

    wines = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            wines = wines.filter(queries)

    context = {
        'wines': wines,
        'search_term': query,
    }

    return render(request, 'products/wines.html', context)

def wine_detail(request, product_id):
    """A view to show product details """

    wine = get_object_or_404(Product, pk=product_id)

    context = {
        'wine': wine,
    }

    return render(request, 'products/wine_detail.html', context)