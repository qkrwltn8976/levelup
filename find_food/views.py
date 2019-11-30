from django.shortcuts import render
from .models import Vendor, Location
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer
# Create your views here.
def home(request):
    vendor = Vendor.objects
    location = Location.objects.all()
    return render(request, 'home.html',{'location':location})

def map(request):
    return render(request, 'map.html')

@api_view(['POST'])
def select_loc(request, loc_id):
    if request.method == 'POST':
        location = Location.objects.get(pk=loc_id)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
