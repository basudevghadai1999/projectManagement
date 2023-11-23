from django.urls import path
from . import views

urlpatterns = [
	path('users/', views.userOverview, name="user-overview"),
	path('user-list/', views.userList, name="user-list"),
	path('user-detail/<str:pk>/', views.userDetail, name="user-detail"),
	path('user-create/', views.userCreate, name="user-create"),

	path('user-update/<str:pk>/', views.userUpdate, name="user-update"),
	path('user-delete/<str:pk>/', views.userDelete, name="user-delete"),
]
