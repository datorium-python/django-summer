from django.urls import path

from shop import views

urlpatterns = [
    path('<int:product_id>/', views.ProductView.as_view(), name='product-detail'),
    path('', views.ProductsView.as_view(), name='products'),
    path('cart/', views.CartView.as_view(), name='cart'),
]
