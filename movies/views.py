from django.shortcuts import render
from rest_framework import viewsets
from .model import MovieData
from .serializers import MovieSerializer


class MovieViewSet(viewsets.MovieSerializer):
    queryset = MovieData
    serializers = MovieSerializer