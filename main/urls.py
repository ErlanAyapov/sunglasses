from django.urls import path
from . import views


urlpatterns = [
	path('', views.MainView.as_view(), name = 'home'),
	path('make-order/', views.order_view, name = 'make_order'),
	path('order/$^@-?*#&?!--?*#&?!?-?*#&?!*', views.OrdersPage.as_view(), name = 'order_page'),
	path('order/comp/*#&?!---?*#?*#&<int:pk>*#-*#&?!--?*#-?*#&/', views.OrderUpdateView.as_view(), name = 'order_update'),
	path('order/*#&?*#&?!?#&#?*#&?<int:pk>?*#&?!??#&?!?-#/', views.OrderDetailView.as_view(), name = 'order_detail'),
	path('success/', views.success_page, name = 'success'),
	path('cart/add/', views.CartAddView, name = 'cart_add'),
	path('my-orders/?#&#!?!*#&?<int:pk>?#&#?*#&?', views.CartView.as_view(), name = 'my_orders'),
]