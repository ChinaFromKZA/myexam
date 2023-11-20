from django.urls import path
from . import views

urlpatterns = [
    path('', views.price, name='price'),
    path('create', views.create, name='create'),
    path('bdtick/<int:pk>/', views.PriceDetailView.as_view(), name='price_details'),
    path('delete/<int:price_id>/', views.delete_price, name='delete_price'),
]