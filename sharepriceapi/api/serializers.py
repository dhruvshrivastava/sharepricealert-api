from rest_framework import serializers 
from .models import Watchlist, Ticker
from django.contrib.auth.models import User

class WatchlistSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    

    class Meta:
        model = Watchlist 
        fields = [
            'created_by',
            
        ]
class UserSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = User
        fields = ['id','username','email','password']

class TickerSerializer(serializers.ModelSerializer):
    watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Ticker
        fields = ['ticker_name','watchlist']


