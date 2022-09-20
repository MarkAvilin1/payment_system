import stripe
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Product

stripe.api_key = 'sk_test_51LihR8C3sm9WglDW7NGUPve1pdakG8a11JVEshxwiXGy0J6ozBs0qEyaeADX6ZNw1clPfTP1IfkM8CgBPkT7w' \
                 'lMN00YVJ35K5k'


def store(request):
    products = Product.objects.all().filter(is_available=True)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj
    }
    return render(request, 'store.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)


def buy(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'buy.html', context)


def payment(request, pk):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        print(pk)
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description="Payment"
        )
    item = Product.objects.get(id=pk)
    item.quantity -= 1
    item.save()
    return render(request, 'success.html')


def success(request):
    return render(request, 'success.html')


def wrong(request):
    return render(request, 'wrong.html')
