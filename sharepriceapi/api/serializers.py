from rest_framework import serializers 
from .models import Watchlist

class WatchlistSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()

    class Meta:
        model = Watchlist 
        fields = [
            'created_by',
            'tickers'
        ]