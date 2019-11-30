from django.shortcuts import render
from .models import Vendor, Location
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer
from .serializers import VendorSerializer
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
        vendor = Vendor.objects.filter(loc=loc_id)
        print(vendor[0].position_x)
        serializer = LocationSerializer(location)
        serializer_v = VendorSerializer(vendor, many=True) 
        Serializer_list = [serializer.data, serializer_v.data]

        content = {
            'data': Serializer_list,
        }
        return Response(content)
