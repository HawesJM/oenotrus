from django.shortcuts import render

# Create your views here.

def index(request):
    """a view to return index page"""
    
    return render(request, 'home/index.html')


# custom 404 view
def custom_404(request, exception):
    return render(request, 'home/404.html', status=404)