from rest_framework import serializers 
from .models import Ticker, FrequencyAlerts, VolumeAlerts, PercentageAlerts
from django.contrib.auth.models import User

class TickerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticker
        fields = ['ticker_name', 'watchlist_of']


class UserSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = User
        fields = ['id','username','email','password']

class FrequencySerializer(serializers.ModelSerializer):


    class Meta:
        model = FrequencyAlerts
        fields = ['ticker', 'interval','time_set', 'alert_of']

class VolumeSerializer(serializers.ModelSerializer):


    class Meta:
        model = VolumeAlerts
        fields = ['ticker', 'limit', 'alert_of']

class PercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PercentageAlerts
        fields = ['ticker', 'limit', 'alert_of']




