from django.shortcuts import render, redirect
from django.views import View

from products.models import Product


class SearchView(View):

    def get(self, request):
        search_term = request.GET['query']
        if search_term == '':
            return redirect('home')
        products = Product.objects.filter(title__icontains=search_term)
        return render(request, 'search/search.html', {'products': products})
