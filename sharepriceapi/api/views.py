from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .serializers import TickerSerializer, UserSerializer, FrequencySerializer, TriggerSerializer, VolumeSerializer, PercentageSerializer
from .models import Ticker, FrequencyAlerts, PercentageAlerts, VolumeAlerts, TriggerAlerts
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


class TriggerViewset(viewsets.ModelViewSet):
    queryset = TriggerAlerts.objects.all()
    serializer_class = TriggerSerializer
    permission_classes = {IsAuthenticatedOrReadOnly,}

    def perform_create(self, serializer):
        serializer.save(ticker=self.request.data['ticker'], above_limit = self.request.data['above_limit'], below_limit = self.request.data['below_limit'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
