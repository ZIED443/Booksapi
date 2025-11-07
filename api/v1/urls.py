from django.urls import path, include

urlpatterns = [
    path('users/', include('api.v1.users.urls')),
    path('bookstore/', include('api.v1.bookstore.urls')),
    path('reservations/', include('api.v1.reservations.urls')),
]