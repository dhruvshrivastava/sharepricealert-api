from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework.views import APIView
from .permissions import OnlyOwner
from rest_framework.response import Response
from .serializers import TickerSerializer, UserSerializer
from .models import Ticker
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    permission_classes = {IsAuthenticatedOrReadOnly,}

    def perform_create(self, serializer):
        serializer.save(ticker_name=self.request.data['ticker_name'])


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        username = self.request.data['username']
        email = self.request.data['email']
        password = make_password(self.request.data['password'])
        User.objects.create(username=username, email=email, password=password)
        serializer.save(username=username, email=email, password=password)

