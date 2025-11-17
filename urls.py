from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpanel/', include('adminpanel.urls')),  # tambahkan ini
]

