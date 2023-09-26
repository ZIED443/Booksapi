from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    
)
from . views import *
from . import views

urlpatterns = [
 path('user/' , views.UserList.as_view(), name="user list "),
 path('user/<int:pk>' , views.UserUpdate.as_view(), name="User update"),
 path('books/',views.Booklist.as_view(),name="books list"),
 path('book/<int:pk>', views.BookUpdate.as_view(),name="book update"),
 path('author/',views.AuthorList.as_view(),name="Authors list "),
 path('author/<int:pk>',views.Authorupdate.as_view(),name="Authors update "),
 path('reservation/' , views.ReservationList.as_view(), name="reservation list "),
 path('reservation/<int:pk>' , views.ReservationUpdate.as_view(), name="reservation update "),

 path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 path('token/verify/', views.MyTokenVerifyView.as_view(), name='token_verify'),
 path('token/',views.MyTokenObtainPairView.as_view(),name='connexion'),

  
 ]
 