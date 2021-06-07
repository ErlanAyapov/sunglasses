from django import forms
from products.models import Order, QuantityOrder, Cart


class OrderForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['order_date'].label = 'Дата получения заказа'

    # order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'comment', 'product', 'user', 'id'
        )


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = (
            'user', 'product', 'comment'
        )
        # exclude = ['user']


class OrderUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['status']   

class QuantityOrderForm(forms.ModelForm):
    
    class Meta:
        model = QuantityOrder 
        fields = ['product', 'quantity']    