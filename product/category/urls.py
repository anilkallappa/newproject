from django.urls import path
from . import apiviews
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product', apiviews.ProductListView.as_view(), name='product_list1'),

]
