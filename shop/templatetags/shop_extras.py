from django import template

register = template.Library()


def format_price(value, default):  # 100|format_price:"USD"
    currency_symbols = {
        'USD': '$',
    }

    split_value = value.split(' ')

    if len(split_value) == 2:
        price, currency = split_value

    else:
        price = split_value[0]
        currency = default

    symbol = currency_symbols[currency]

    formatted_price = f'{symbol}{price}'

    return formatted_price


register.filter(
    name='format_price',
    filter_func=format_price,
)
