

from rest_framework import generics
from .models import *
from rest_framework.permissions import  IsAuthenticated
from books.serializers import *
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