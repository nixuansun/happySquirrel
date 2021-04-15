from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.contrib import messages

from .models import happySquirrel
# from .forms import st_form


# A view that lists all squirrel sightings with links to view each sighting
def sightings(request):
    squirrels = happySquirrel.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'squirrel/sightings.html', context)



# # A view to update a particular sighting
# def edit(request, squirrel_id):
#     squirrel = get_object_or_404(happySquirrel, unique_squirrel_id=squirrel_id)
    
#     if request.method == 'POST':
#         new = st_form(request.POST, instance = original)
#         if new.is_valid():
#             new.save()
#             context = {
#                     'new':new,
#                     }
#             return redirect('/sightings')
#     else:
#         form = st_form(instance = original)
#     context2 = {
#             'form': form,
#             }
#     return render(request, 'squirrel/info.html', context2)



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


# # A view to create a new sighting
# def add(request):
#     if request.method == 'POST':
#         form = st_form(request.POST)
#         if form.is_valid():
#             form.save()
#             context = {
#                     'form':form,
#                     }
#             return redirect('/sightings')
#     else:
#         form = st_form() 
#     context2 = {
#             'form': form,
#             }
#     return render(request, 'st/add.html', context2)
    


