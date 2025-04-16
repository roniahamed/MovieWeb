from django.urls import path
from . import views
urlpatterns = [
    path('', views.movie_data, name='movie_list')
]