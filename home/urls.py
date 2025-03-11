from tkinter.font import names

from django.urls import path
from . import views
from .views import UserUpdate, SearchList, PartsList

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/update/<int:pk>/', UserUpdate.as_view(), name='update_profile'),
    path('profile/', views.login_profile, name='login_profile'),
    path('search/', SearchList.as_view(), name='search'),
    path('parts-list/', PartsList.as_view(), name='parts-list'),
    ]