from django.shortcuts import render
from rest_framework import viewsets
from .models import MovieData
# from .serializers import MovieSerializer


# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = MovieData.objects.all()
#     serializer_class = MovieSerializer


# class ActionViewSet(viewsets.ModelViewSet):
#     queryset = MovieData.objects.filter(typ='action')
#     serializer_class = MovieSerializer


# class ComedyMovie(viewsets.ModelViewSet):
#     queryset = MovieData.objects.filter(typ='comedy')
#     serializer_class = MovieSerializer


def movie_data(request):
    movie_objects = MovieData.objects.all()
    return render(request, 'movies/movie_list.html',{'movie_objects':movie_objects})