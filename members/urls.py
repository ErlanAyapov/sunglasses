from django.urls import path
from . import views


urlpatterns = [
	path('', views.members_view, name = 'members'),
	path('register/', views.register, name = 'register'),
	path('auth/', views.authentication, name = 'auth'),
	path('logout/', views.logout, name = 'logout')
]