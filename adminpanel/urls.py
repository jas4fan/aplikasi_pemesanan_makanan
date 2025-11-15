from django.urls import path
from . import views

app_name = "adminpanel"

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    path('add-user/', views.add_user, name='add_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add-driver/', views.add_driver, name='add_driver'),
    path('toggle-driver/<int:driver_id>/', views.toggle_driver, name='toggle_driver'),
    path('delete-rating/<int:rating_id>/', views.delete_rating, name='delete_rating'),
    path('', views.index, name='index'),
]

