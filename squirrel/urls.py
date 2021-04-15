from django.urls import path

from . import views


urlpatterns = [
    path('', views.sightings, name='sightings'),
    path('<squirrel_id>/', views.update, name='update'),
    path('add/', views.add, name='add'),
#     path('stats/', views.showstats, name='showstats'),
]
