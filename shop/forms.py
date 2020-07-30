from django import forms


class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(
        required=True,
        widget=forms.HiddenInput(),
    )
