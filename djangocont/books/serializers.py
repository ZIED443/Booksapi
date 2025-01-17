from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenVerifySerializer
from rest_framework import exceptions

from django.conf import settings
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.exceptions import TokenError
class UserSerializer(serializers.ModelSerializer) : 
    
     class Meta : 
        model = User
   
        fields = [
                 'id',
                 'is_staff',
                 'is_active' ,
                 'user_name' ,
                 'email',
                 'password',
                 'sex'
        ]  
class AuthorSerializer(serializers.ModelSerializer):  
     

        class Meta : 
          model = Author      
          fields = [
                'id',
                'name',
                'birthday',
              
        
               
        ]
        

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        authorname = serializers.SerializerMethodField()

        fields = [
         'id',
         'author' ,
         'authorname', 
         'date_release',
         'name'
         ]
    def get_authorname(self, obj):
        return obj.author.name if obj.author else None
class BookReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookreservation

        fields = [
         'id',
         'user' ,
         'book',
         'date1',
         'date2' ,
         'username',
         'book_title'
         ]
    def get_username(self, obj):
        return obj.user.username if obj.user else None
    
    def get_book_title(self, obj):
        return obj.book.name if obj.book else None



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        access_token = refresh.access_token
        if not access_token.is_valid():
            raise exceptions.AuthenticationFailed('Access token is invalid')
        
        return data

class MyTokenVerifySerializer(TokenVerifySerializer):
    token = serializers.CharField()

    def validate(self, attrs):
        try:
            token = Token(attrs['token'], key=settings.SECRET_KEY, algorithms=['HS256'])
            token_data = token.payload
            user_id = token_data.get('user_id')

            user = User.objects.get(id=user_id)


            return {'user': user, 'token': token_data}
        except TokenError:
            raise serializers.ValidationError('Invalid token')
        except User.DoesNotExist:
            raise serializers.ValidationError('User not found')
