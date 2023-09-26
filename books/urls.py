from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    
)
from . views import *
from . import views

urlpatterns = [
 path('api/user/' , views.UserList.as_view(), name="user list "),
 path('api/user/<int:pk>' , views.UserUpdate.as_view(), name="User update"),
 path('api/books/',views.Booklist.as_view(),name="books list"),
 path('api/book/<int:pk>', views.BookUpdate.as_view(),name="book update"),
 path('api/author/',views.AuthorList.as_view(),name="Authors list "),
 path('api/author/<int:pk>',views.Authorupdate.as_view(),name="Authors update "),
 path('api/reservation/' , views.ReservationList.as_view(), name="reservation list "),
 path('api/reservation/<int:pk>' , views.ReservationUpdate.as_view(), name="reservation update "),

 path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 path('api/token/verify/', views.MyTokenVerifyView.as_view(), name='token_verify'),
 path('api/token/',views.MyTokenObtainPairView.as_view(),name='connexion'),

  
 ]
 