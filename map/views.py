from django.shortcuts import render

from squirrel.models import happySquirrel

# Create your views here.
def map(request):
    map_ = happySquirrel.objects.all()[:100]
    return render(request, 'map/map.html', {"map_squirrel":map_})
