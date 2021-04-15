from django.shortcuts import render

from sightings.models import data

# Create your views here.
def map(request):
    map_ = data.objects.all()[:100]
    return render(request, 'map/map.html', {"map_squirrel":map_})
