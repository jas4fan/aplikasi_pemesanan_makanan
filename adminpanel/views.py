from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Driver, Rating
from django.urls import reverse
from django.db import IntegrityError

def admin_dashboard(request):
    users = User.objects.all()
    drivers = Driver.objects.select_related('user').all()
    ratings = Rating.objects.select_related('target_user').order_by('-created_at')[:100]

    context = {
        "users": users,
        "drivers": drivers,
        "ratings": ratings,
    }
    return render(request, "adminpanel/index.html", context)


def add_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        role = request.POST.get("role")
        try:
            user = User.objects.create(name=name, email=email, role=role)
            # jika role driver, create Driver entry juga
            if role == "driver":
                Driver.objects.create(user=user)
        except IntegrityError:
            # bisa tambahkan pesan error di template, tapi untuk simpel kita ignore
            pass
    return redirect(reverse("adminpanel:dashboard"))


def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect(reverse("adminpanel:dashboard"))


def add_driver(request):
    # support menambah driver yang sudah ada user atau bikin user sekaligus
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        if user_id:
            user = get_object_or_404(User, id=user_id)
            user.role = "driver"
            user.save()
            Driver.objects.get_or_create(user=user)
        else:
            # create new user + driver
            name = request.POST.get("name")
            email = request.POST.get("email")
            user = User.objects.create(name=name, email=email, role="driver")
            Driver.objects.create(user=user)
    return redirect(reverse("adminpanel:dashboard"))


def toggle_driver(request, driver_id):
    d = get_object_or_404(Driver, id=driver_id)
    d.is_active = not d.is_active
    d.save()
    return redirect(reverse("adminpanel:dashboard"))


def delete_rating(request, rating_id):
    Rating.objects.filter(id=rating_id).delete()
    return redirect(reverse("adminpanel:dashboard"))

def index(request):
    return render(request, 'index.html')

