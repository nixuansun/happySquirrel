from django.urls import path

from . import views


urlpatterns = [
    path('', views.sightings, name='sightings'),
    path('<unique_squirrel_id>/', views.update, name='update'),
#     path('stats/', views.showstats, name='showstats'),
#     path('add/', views.add, name='add'),
]
