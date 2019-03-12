from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product

from datetime import datetime

def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})

@login_required
def create(request):
    if request.method == 'POST':
        product = Product()
        if request.POST['title'] != '' and request.POST['url'] != '' and request.POST['body'] != '' and 'image' in request.FILES and 'icon' in request.FILES:
            product.title = request.POST['title']
            product.url = request.POST['url']
            product.pub_date = datetime.now()
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.body = request.POST['body']
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': {
                'title': 'Error',
                'message': 'Complete the form'
            }})

        return redirect('home')
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})

@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total = product.votes_total + 1
        product.save()
        return redirect('/products/' + str(product.id))