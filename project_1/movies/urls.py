from django.urls import path
from . import views
app_name = 'movies'


urlpatterns = [
    path('', views.movies_list, name="list"),
    path('review/', views.create_review, name="review"),
    path('signed_in/', views.movies_list_signed_in, name="signed_in"),
    path('signed_in/<slug:slug>/', views.movie_detail_signed_in, name="details_signed_in"),
    path('<slug:slug>/', views.movie_detail, name="detail")
]