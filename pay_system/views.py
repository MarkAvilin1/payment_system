from django.core.paginator import Paginator
from django.shortcuts import render

from store.models import Product


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj
    }
    return render(request, 'index.html', context)
