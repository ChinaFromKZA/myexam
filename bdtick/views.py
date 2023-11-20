from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductsForm
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, redirect


def price(request):
    prices = Products.objects.all()
    return render(request, 'bdtick/price.html', {'prices': prices})


class PriceDetailView(DetailView):
    model = Products
    template_name = 'bdtick/details_view.html'
    context_object_name = 'course'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Заполненная вами форма ошибочная'
    else:
        form = ProductsForm()

    lists = {
        'form': form,
        'error': error
    }

    return render(request, 'bdtick/create.html', lists)


def delete_price(request, price_id):
    price = get_object_or_404(Products, pk=price_id)
    if request.method == 'POST':
        price.delete()
        return redirect('price')
    return redirect('price_details', pk=price_id)
