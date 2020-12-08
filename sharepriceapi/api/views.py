from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated 

from .serializers import WatchlistSerializer
from .models import Watchlist

class WatchlistViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

    
