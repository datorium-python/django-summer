from django.http import HttpResponse

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from shop import (
    models,
    forms,
)


class ProductsView(ListView):
    model = models.Product
    template_name = 'shop/products.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.select_related()

        return queryset


class ProductView(DetailView):
    pk_url_kwarg = 'product_id'
    model = models.Product
    template_name = 'shop/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = context['product']

        context['test_price'] = f'{product.price} USD'

        form = forms.AddToCartForm()
        form.fields['product_id'].initial = str(product.id)

        context['form'] = form

        return context


class CartView(View):
    def get(self, request):
        cart_id = request.session.get('cart_id', None)

        cart = get_object_or_404(
            klass=models.Cart,
            pk=cart_id,
        )

        context = {
            'cart': cart,
        }

        return render(
            request=request,
            template_name='shop/cart.html',
            context=context,
        )

    def post(self, request):
        cart_id = request.session.get('cart_id', None)

        if cart_id is None:
            cart = models.Cart.objects.create()

            request.session['cart_id'] = str(cart.id)

        else:
            cart = models.Cart.objects.get(pk=cart_id)

        form = forms.AddToCartForm(data=request.POST)

        if form.is_valid():
            product_id = form.cleaned_data['product_id']

            product = get_object_or_404(
                klass=models.Product,
                pk=product_id,
            )

            cart.products.add(product)

            return redirect(to='cart')
