from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'onlinestore'
urlpatterns = [
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
]