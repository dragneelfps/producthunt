from django.shortcuts import render

def home(request):
    return render(request, 'products/home.html')

def create(request):
    if request.method == 'POST':
        print('req', request.POST);
        return render(request, 'products/create.html')
    else:
        return render(request, 'products/create.html')
