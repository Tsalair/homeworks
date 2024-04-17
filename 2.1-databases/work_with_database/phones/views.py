from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'     
    phone_sort = request.GET.get('sort', default=None)
    if phone_sort == 'name':
        phones = Phone.objects.order_by('name')
    elif phone_sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif phone_sort == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()
    context = {'phones':phones}
      
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone':phone}
    return render(request, template, context)
