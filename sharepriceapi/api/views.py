from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework.views import APIView
from .permissions import OnlyOwner
from rest_framework.response import Response
from .serializers import WatchlistSerializer, UserSerializer
from .models import Watchlist
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = {IsAuthenticatedOrReadOnly, OnlyOwner}

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        username = self.request.data['username']
        email = self.request.data['email']
        password = make_password(self.request.data['password'])
        User.objects.create(username=username, email=email, password=password)
        serializer.save(username=username, email=email, password=password)