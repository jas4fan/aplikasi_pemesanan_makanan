from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.orders_view, name="order_supervisor"),
    path("orders/delete/<int:order_id>/", views.delete_order, name="delete_order"),

    path("ratings/", views.ratings_view, name="rating_moderator"),
    path("ratings/delete/<int:rating_id>/", views.delete_rating, name="delete_rating"),

    path("restaurant/", views.restaurant_manager_view, name="restaurant_manager"),
]

