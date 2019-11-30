from django.shortcuts import render
from .models import Vendor, Location
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer
# from .forms import PostForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        
        loc = request.POST.getlist("location")
        vendor = Vendor.objects.filter(loc__name__in = loc)
        location = Location.objects.all()
        print(vendor)
        return render(request, 'map.html', {'location':location, 'vendor':vendor})
        pass
    else:
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
