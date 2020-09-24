from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos', views.ProductListView.as_view(), name='producto_list'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='producto_detail'),
]