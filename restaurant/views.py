from django.shortcuts import render
from rest_framework import authentication
from .models import Booking,Menu
from rest_framework.permissions import IsAuthenticated
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
    