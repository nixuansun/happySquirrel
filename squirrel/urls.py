from django.urls import path

from . import views


urlpatterns = [
    path('', views.sightings, name='sightings'),
    path('add/', views.add, name='add'),
    path('<squirrel_id>/', views.update, name='update'),
    path('stats', views.stats, name = 'stats'),
]
