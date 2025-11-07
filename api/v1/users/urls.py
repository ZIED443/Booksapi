
from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list-create'),  # GET / POST
    path('<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view(), name='user-detail'),  # GET / PUT / PATCH / DELETE
]
