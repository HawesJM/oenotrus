from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import WineForm

def all_wines(request):
    """A view to show all wines and allow sorting and searching """

    wines = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET ['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                wines = wines.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            wines = wines.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            wines = wines.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria")
                return redirect(reverse('wines'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            wines = wines.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'wines': wines,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/wines.html', context)

def wine_detail(request, product_id):
    """A view to show product details """

    wine = get_object_or_404(Product, pk=product_id)

    context = {
        'wine': wine,
    }

    return render(request, 'products/wine_detail.html', context)


def add_wine(request):
    """ Add a wine to the store """
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added wine!')
            return redirect(reverse('add_wine'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = WineForm()
        
    template = 'products/add_wine.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_wine(request, product_id):
    """ Edit a wine in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'wine successfully updated!')
            return redirect(reverse('wine_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update wine. Please ensure the form is valid.')
    else:
        form = WineForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_wine.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

def delete_wine(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'wine deleted!')
    return redirect(reverse('wines'))