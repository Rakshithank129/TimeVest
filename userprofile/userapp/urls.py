from django.urls import path
from userapp import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.user_logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('update',views.update,name='update'),
    path('investment',views.investment_view,name='investment')
]