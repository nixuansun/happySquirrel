from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.contrib import messages

from .models import happySquirrel
from .forms import squirrelUpdateForm


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
    form = squirrelUpdateForm() 
    context = {
        'form': form,
    }
    return render(request, 'squirrel/sightings/add.html', context)



# # A view with general stats about the sightings
# def showstats(request):
#     squirrel = happySquirrel.objects.all()
#     count_shift = squirrel.values('shift').order_by('shift').annotate(shift_count = Count('shift'))
#     count_adult = happySquirrel.objects.filter(age='Adult').count()
#     count_juvenile = happySquirrel.objects.filter(age='Juvenile').count()
#     count_above = happySquirrel.objects.filter(location='Above Ground').count()
#     count_plane = happySquirrel.objects.filter(location='Ground Plane').count()
#     count_running = happySquirrel.values('running').annotate(count_running=Count('running')).filter(running="True")
#     count_eating = happySquirrel.values('eating').annotate(count_eating=Count('eating')).filter(eating="True")
#     context = {
#         'count_shift':count_shift,
#         'count_adult':count_adult,
#         'count_juvenile': count_juvenile,
#         'count_above':count_above,
#         'count_plane': count_plane,
#         'count_running':count_running,
#         'count_eating':count_eating,
#         }
#     return render(request,'st/stats.html',context)
