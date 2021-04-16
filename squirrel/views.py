from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Avg, Max, Min, Count
from django.contrib import messages

from .models import happySquirrel
from .forms import squirrelUpdateForm, squirrelAddForm


# A view that lists all squirrel sightings with links to view each sighting
def sightings(request):
    squirrels = happySquirrel.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'squirrel/sightings.html', context)



# A view to update a particular sighting
def update(request, squirrel_id):
    squirrel = get_object_or_404(happySquirrel, unique_squirrel_id=squirrel_id)
    form = squirrelUpdateForm(instance=squirrel)
    context = {
        'form': form,
    }
    return render(request, 'squirrel/update.html', context)



# A view to create a new sighting
def add(request):
	if request.method=='Post':
		form = squirrelAddForm(request.POST) 
		if form.is_valid():
			form.save()
			return redirect('f/sightings/')
	else:
		form = squirrelAddForm()
		context = {
			'form': form,
		}
		return render(request, 'squirrel/add.html', context)



# A view with general stats about the sightings
def stats(request):
	squirrels = happySquirrel.objects.all()
	total = len(squirrels)
	count_adult = squirrels.filter(age='Adult').count()
	count_juvenile = squirrels.filter(age='Juvenile').count()
	count_running = squirrels.values('running').annotate(count_running=Count('running')).filter(running="True")
	count_eating = squirrels.values('eating').annotate(count_eating=Count('eating')).filter(eating="True")
	lat=squirrels.aggregate(min_latitude=Min('latitude'),max_latitude=Max('latitude'),average_latitude=Avg('latitude'))
    	long=squirrels.aggregate(min_longitude=Min('longitude'),max_longitude=Max('longitude'),average_longitude=Avg('longitude'))
	context = {
		'total': total,
		'adult': count_adult,
		'juvenile': count_juvenile,
		'running': count_running,
		'eating': count_eating
		'latitude': lat,
		'longitude': long
	}
	return render(request, 'squirrel/stats.html', context)
