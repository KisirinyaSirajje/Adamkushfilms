
from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()  # Fetch all movie records
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Create your views here.
