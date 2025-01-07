

from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import  IsAuthenticated , AllowAny
from books.serializers import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenVerifyView)
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import DateField

class Booklist(generics.ListCreateAPIView):    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
   
class BookUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [AllowAny]    

class AuthorList(generics.ListCreateAPIView):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
   
class Authorupdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer  
    permission_classes = [AllowAny]
    
class UserList(generics.ListAPIView):
     
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer  
    permission_classes = [AllowAny]

class ReservationList(generics.ListCreateAPIView):
    
    queryset = Bookreservation.objects.all()
    serializer_class = BookReservationSerializer  
    permission_classes = [AllowAny]

class ReservationUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Bookreservation.objects.all()
    serializer_class = BookReservationSerializer  
    permission_classes = [AllowAny]    


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer   

class MyTokenVerifyView(TokenVerifyView):
   serializer_class=MyTokenVerifySerializer     


class ReservationSelect(APIView):
    def get(self, request):
        d1 = self.request.query_params.get('d1' , datetime.now())
        d2 = self.request.query_params.get('d2' ,  datetime.now())
        
        reservations = Bookreservation.objects.filter(date1__lte=d1, date2__gte=d2)
        
        serializer = BookReservationSerializer(reservations, many=True)
        
        return Response(serializer.data)
