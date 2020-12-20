from rest_framework import serializers 
from .models import Watchlist, Ticker, Alerts, FrequencyAlerts, VolumeAlerts, PercentageAlerts
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
    watchlist = serializers.ReadOnlyField(source="watchlist.created_by")
    
    class Meta:
        model = Ticker
        fields = ['ticker_name','watchlist']

class AlertsSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username", read_only=True)

    class Meta:
        model = Alerts
        fields = [
            'created_by',
        ]


class FrequencySerializer(serializers.ModelSerializer):
    alert = serializers.ReadOnlyField(source="alert.created_by")

    class Meta:
        model = FrequencyAlerts
        fields = ['ticker', 'interval','time_set', 'alert']

class VolumeSerializer(serializers.ModelSerializer):
    alert = serializers.ReadOnlyField(source="alert.created_by")

    class Meta:
        model = VolumeAlerts
        fields = ['ticker', 'limit', 'alert']

class PercentageSerializer(serializers.ModelSerializer):
    alert = serializers.ReadOnlyField(source="alert.created_by")

    class Meta:
        model = PercentageAlerts
        fields = ['ticker', 'limit', 'alert']



