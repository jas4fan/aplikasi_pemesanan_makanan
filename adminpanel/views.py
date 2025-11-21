from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Rating, RestaurantInfo

# ============================
# Orders CRUD
# ============================

def orders_view(request):
    orders = Order.objects.all()

    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        item_name = request.POST.get("item_name")
        quantity = request.POST.get("quantity")

        Order.objects.create(
            customer_name=customer_name,
            item_name=item_name,
            quantity=quantity
        )
        return redirect("order_supervisor")

    return render(request, "adminpanel/orders.html", {"orders": orders})

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect("order_supervisor")


# ============================
# Ratings CRUD
# ============================

def ratings_view(request):
    ratings = Rating.objects.all()

    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Rating.objects.create(
            customer_name=customer_name,
            rating=rating,
            comment=comment
        )
        return redirect("rating_moderator")

    return render(request, "adminpanel/ratings.html", {"ratings": ratings})

def delete_rating(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    rating.delete()
    return redirect("rating_moderator")


# ============================
# Restaurant Info (Edit only)
# ============================

def restaurant_manager_view(request):
    info = RestaurantInfo.objects.first()

    if info is None:
        info = RestaurantInfo.objects.create(
            restaurant_name="My Restaurant",
            address="Unknown",
            open_hours="08.00 - 22.00"
        )

    if request.method == "POST":
        info.restaurant_name = request.POST.get("restaurant_name")
        info.address = request.POST.get("address")
        info.open_hours = request.POST.get("open_hours")
        info.save()
        return redirect("restaurant_manager")

    return render(request, "adminpanel/restaurant.html", {"info": info})


def index(request):
    return render(request, 'adminpanel/index.html')

