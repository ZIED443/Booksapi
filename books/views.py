

from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import  IsAuthenticated
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
    permission_classes = [IsAuthenticated]
   
class BookUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]    

class AuthorList(generics.ListCreateAPIView):
    
    queryset = Auhor.objects.all()
    serializer_class = AuhorSerializer
    permission_classes = [IsAuthenticated]
   
class Authorupdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Auhor.objects.all()
    serializer_class = AuhorSerializer  
    permission_classes = [IsAuthenticated]
    
class UserList(generics.ListAPIView):
     
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer  
    permission_classes = [IsAuthenticated]

class ReservationList(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Bookreservation.objects.all()
    serializer_class = BookReservationSerializer  
    permission_classes = [IsAuthenticated]

class ReservationUpdate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Bookreservation.objects.all()
    serializer_class = BookReservationSerializer  
    permission_classes = [IsAuthenticated]    


class MyTokenObtainPairView(TokenObtainPairView):
    #authentification with token
    serializer_class = MyTokenObtainPairSerializer   

class MyTokenVerifyView(TokenVerifyView):
   serializer_class=MyTokenVerifySerializer     



class ReservationSelect(APIView):
    def get(self, request):
        d1 = self.request.query_params.get('d1')
        d2 = self.request.query_params.get('d2')
        
        reservations = Bookreservation.objects.filter(date1__lte=d1, date2__gte=d2)
        
        serializer = BookReservationSerializer(reservations, many=True)
        
        return Response(serializer.data)
