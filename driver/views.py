from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DriverLoginForm, DriverRegistrationForm, DriverProfileForm
from .models import DriverProfile

def login_view(request):
    if request.user.is_authenticated:
        return redirect('driver:dashboard')
    
    if request.method == 'POST':
        form = DriverLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('driver:dashboard')
    else:
        form = DriverLoginForm()
    
    return render(request, 'driver/login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('driver:dashboard')
    
    if request.method == 'POST':
        user_form = DriverRegistrationForm(request.POST)
        profile_form = DriverProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Simpan user baru
            user = user_form.save()
            
            # Simpan profile driver
            driver_profile = profile_form.save(commit=False)
            driver_profile.user = user
            driver_profile.save()
            
            messages.success(request, 'Registrasi berhasil! Silakan login.')
            return redirect('driver:login')
        else:
            # Tampilkan error
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            for field, errors in profile_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        user_form = DriverRegistrationForm()
        profile_form = DriverProfileForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'driver/register.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout berhasil!')
    return redirect('driver:login')

@login_required(login_url='driver:login')
def dashboard(request):
    # Auto-create DriverProfile jika belum ada
    driver, created = DriverProfile.objects.get_or_create(user=request.user)
    
    # Placeholder untuk order (setelah Order model dibuat tim lain)
    unassigned_orders = []
    assigned_orders = []
    
    context = {
        'driver': driver,
        'unassigned_orders': unassigned_orders,
        'assigned_orders': assigned_orders,
    }
    return render(request, 'driver/dashboard.html', context)

@login_required(login_url='driver:login')
def order_detail(request, order_id):
    driver, _ = DriverProfile.objects.get_or_create(user=request.user)
    
    context = {
        'driver': driver,
    }
    return render(request, 'driver/order_detail.html', context)

@login_required(login_url='driver:login')
def accept_order(request, order_id):
    if request.method == 'POST':
        driver, _ = DriverProfile.objects.get_or_create(user=request.user)
        messages.success(request, 'Order berhasil diterima!')
    
    return redirect('driver:dashboard')

@login_required(login_url='driver:login')
def start_delivery(request, order_id):
    if request.method == 'POST':
        messages.success(request, 'Pengiriman dimulai!')
    
    return redirect('driver:dashboard')

@login_required(login_url='driver:login')
def complete_order(request, order_id):
    if request.method == 'POST':
        messages.success(request, 'Order berhasil dikirim!')
    
    return redirect('driver:dashboard')
