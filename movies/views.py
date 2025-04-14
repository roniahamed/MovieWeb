from django.shortcuts import render
from rest_framework import viewsets
from .model import MovieData
from .serializers import MovieSerializer


class MovieViewSets(viewsets.MovieSerializer):
    queryset = MovieData
    serializers = MovieSerializer