from django.contrib import admin

from shop import models


class ProductAdmin(admin.ModelAdmin):
    # list_display = (
    #     'name',
    #     'price',
    # )
    list_select_related = True


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)
