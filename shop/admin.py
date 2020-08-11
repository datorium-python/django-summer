from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html

from shop import models


def colorize_price(obj: models.Product):
    product_price = obj.price

    if product_price > 100:
        color = 'red'

    else:
        color = 'green'

    html_template = '<span style="color: {};">{}</span>'

    return format_html(
        html_template,
        color,
        product_price,
    )


colorize_price.short_description = 'Colorized Price'


def today(obj):
    return str(timezone.now())


today.short_description = 'Current Time'


class ProductAdmin(admin.ModelAdmin):
    def make_free(self, request, queryset):
        updated = queryset.update(price='0.00')

        self.message_user(
            request=request,
            message='{} products were successfully marked as free.'.format(updated),
            level=messages.SUCCESS,
        )

    make_free.short_description = 'Mark selected products as free'

    actions = [
        make_free,
    ]

    fieldsets = (
        (
            'Basic Information', {
                'fields': (
                    'name',
                    'price',
                ),
            },
        ),

        (
            'Extended Information', {
                'fields': (
                    'user',
                    'description',
                    'image',
                    'categories',
                ),
            },
        ),
    )

    list_display = (
        'user',
        'name',
        'price',

        today,
        colorize_price,
    )

    list_filter = (
        'user__email',
    )

    raw_id_fields = (
        'user',
    )

    readonly_fields = (
        'price',
    )

    search_fields = (
        'name',
        'user__email',
    )

    def view_on_site(self, obj: models.Product):
        url = reverse('product-detail', kwargs={'product_id': obj.id})

        return url


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)
admin.site.register(models.Cart)
