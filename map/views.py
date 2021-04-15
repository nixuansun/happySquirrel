from django.shortcuts import render

from squirrel.models import happySquirrel

# Create your views here.
def map(request):
    squirrels = happySquirrel.objects.all()[:100]
	context = {'squirrels': squirrels}
	return render(request, 'map/map.html', context)
