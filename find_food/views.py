from django.shortcuts import render
from .models import Vendor, Location
# Create your views here.
def home(request):
    vendor = Vendor.objects
    location = Location.objects
    return render(request, 'home.html',{'vendor':vendor, 'location':location})