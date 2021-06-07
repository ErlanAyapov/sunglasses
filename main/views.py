from django.shortcuts import render, redirect
from products.models import Product, Order, QuantityOrder, Cart
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .forms import OrderForm, OrderUpdateForm, QuantityOrderForm, CartForm
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User



# Create your views here.
# def MainView(request):
# 	return render(request, 'main/index.html')

class MainView(ListView):
	model = Product
	template_name = 'main/index.html'
	
	# def get_context_data(self, **kwargs):
	# 	context = super(MainView, self).get_context_data(**kwargs)
	# 	context['comment'] = Comment.objects.all()
	# 	return context


def order_view(request):
	if request.method == 'POST':
		form = OrderForm(request.POST) 
		message = ''
		if form.is_valid():
			form.save(commit = False)
			form.order_date = datetime.datetime.now()
			
			form.save()
			return redirect('success')
			
	form = OrderForm()
	data = {
		'order':form,
	}
	return render(request, 'main/order.html', data)


class OrdersPage(ListView):
	model = Order
	ordering = '-id'
	template_name = 'main/order/order.html'

class OrderUpdateView(UpdateView):
	model = Order
	template_name = 'main/order/update.html'
	form_class = OrderUpdateForm
	def form_valid(self, form):
		form.save()
		return redirect('order_page')

def order_q(request):
	if request.method == 'POST':
		form = QuantityOrderForm(request.POST)

		if form.is_valid():
			form.save()


class OrderDetailView(DetailView):
	model = Order
	template_name = 'main/order/detail.html'


def success_page(request):
	return render(request, 'main/success.html')


def CartAddView(request):
	if request.method == 'POST':
		form = CartForm(request.POST)
		if form.is_valid():
			form.save(commit = False)
			form.user = request.user
			form.save()
			return redirect('home')
		 

	form = CartForm()
	data = {
		'cart_form':form
	}

	return render(request, 'main/cart/add.html', data)


class CartView(ListView):
	model = User 
	template_name = 'main/cart/cart.html'

	def get_context_data(self, **kwargs):
		context = super(CartView, self).get_context_data(**kwargs)
		context['cart'] = Cart.objects.all()
		context['product'] = Product.objects.all()
		return context