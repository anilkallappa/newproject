from django.shortcuts import render
from .models import Category,Product
# Create your views here.
def product_list(request):
    category=Category.objects.all()
    products=Product.objects.all()
    return render(request, 'list.html', {'category': category, 'products': products})