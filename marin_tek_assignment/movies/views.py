from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.views.generic import TemplateView, ListView


# Create your views here.

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = super().get_queryset()
        genre = self.request.GET.get('genre')
        search_query = self.request.GET.get('search')

        if genre:
            queryset = queryset.filter(genres__icontains=genre)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre_list = set()
        for movie in Movie.objects.all():
            genres = movie.genres.split(',')
            genre_list.update([genre.strip() for genre in genres])
        context['genre_list'] = sorted(genre_list)
        return context


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieEditDeleteById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "pk"



class MovieListsView(TemplateView):
    template_name = 'movies/movie_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context

