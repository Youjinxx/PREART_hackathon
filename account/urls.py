from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('mypage/', views.mypage, name = 'mypage'),
    path('mypage_cash/', views.mypage_cash, name = 'mypage_cash'),
]