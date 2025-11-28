from django.urls import path
from . import views

app_name = 'driver'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/accept/', views.accept_order, name='accept_order'),
    path('order/<int:order_id>/start/', views.start_delivery, name='start_delivery'),
    path('order/<int:order_id>/complete/', views.complete_order, name='complete_order'),
]
