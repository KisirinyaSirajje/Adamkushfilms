from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movie_list, name='movie_list'),
]
