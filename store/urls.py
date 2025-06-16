from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),
    path('customer_service', views.customer_service, name='customer_service'),
    path('usage', views.usage, name='usage'),
    path('index', views.index, name='index'),
    path('founders', views.founders, name='founders'),
]