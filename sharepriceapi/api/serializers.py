from rest_framework import serializers 
from .models import Watchlist
from django.contrib.auth.models import User

class WatchlistSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    

    class Meta:
        model = Watchlist 
        fields = [
            'created_by',
            'tickers',
            
        ]
class UserSerializer(serializers.ModelSerializer):
    watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id','username','email','password','watchlist']

