# api/v1//urls.py
from django.urls import path
from .views import ReservationListCreateAPIView, ReservationRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', ReservationListCreateAPIView.as_view(), name='reservation-list-create'),
    path('<int:pk>/', ReservationRetrieveUpdateDeleteAPIView.as_view(), name='reservation-detail'),
]
