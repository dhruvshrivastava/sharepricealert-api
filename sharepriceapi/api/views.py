from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .serializers import TickerSerializer, UserSerializer, WatchlistSerializer, AlertsSerializer, FrequencySerializer, VolumeSerializer, PercentageSerializer
from .models import Ticker, Watchlist, Alerts, FrequencyAlerts, PercentageAlerts, VolumeAlerts
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .permissions import OnlyOwner
from rest_framework.response import Response
from rest_framework import status


class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    permission_classes = {IsAuthenticatedOrReadOnly,}

    def perform_create(self, serializer):
        serializer.save(ticker_name=self.request.data['ticker_name'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        username = self.request.data['username']
        email = self.request.data['email']
        password = make_password(self.request.data['password'])
        User.objects.create(username=username, email=email, password=password)
        serializer.save(username=username, email=email, password=password)

class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = {IsAuthenticatedOrReadOnly, OnlyOwner}

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AlertViewset(viewsets.ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer
    permission_classes = {IsAuthenticatedOrReadOnly, OnlyOwner}

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class FrequencyViewset(viewsets.ModelViewSet):
    queryset = FrequencyAlerts.objects.all()
    serializer_class = FrequencySerializer
    permission_classes = {IsAuthenticatedOrReadOnly,}

    def perform_create(self, serializer):
        serializer.save(ticker=self.request.data['ticker'], interval=self.request.data['interval'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class VolumeViewset(viewsets.ModelViewSet):
    queryset = VolumeAlerts.objects.all()
    serializer_class = VolumeSerializer
    permission_classes = {IsAuthenticatedOrReadOnly,}

    def perform_create(self, serializer):
        serializer.save(ticker=self.request.data['ticker'], limit = self.request.data['limit'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class PercentageViewset(viewsets.ModelViewSet):
    queryset = PercentageAlerts.objects.all()
    serializer_class = PercentageSerializer
    permission_classes = {IsAuthenticatedOrReadOnly,}

    def perform_create(self, serializer):
        serializer.save(ticker=self.request.data['ticker'], limit = self.request.data['limit'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


