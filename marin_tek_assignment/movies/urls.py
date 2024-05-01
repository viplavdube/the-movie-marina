from django.urls import path
from .views import MovieListView, MovieListsView, MovieList, MovieEditDeleteById

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('app_movies/', MovieList.as_view(), name='movie-post-view'),
    path('app_movies/<int:pk>', MovieEditDeleteById.as_view(), name='update'),
]
