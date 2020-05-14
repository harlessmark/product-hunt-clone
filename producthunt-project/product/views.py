from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product


def home(request):
    # get all Product
    products = Product.objects
    return render(request, 'product/home.html', {'products': products})


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.url = request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.hunter = request.user
            product.save()

            return redirect(f'/product/{str(product.id)}')
        else:
            return render(request, 'product/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'product/create.html')


def detail(request, product_id):
    # gets specific product
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/detail.html', {'product': product})


@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect(f'/product/{str(product.id)}')
    else:
        pass
