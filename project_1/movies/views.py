from django.shortcuts import render, HttpResponse, redirect
from .models import Movie, Review
from django.contrib.auth.decorators import login_required
from . import forms


def movies_list(request):
    movies = Movie.objects.all().order_by('date')
    return render(request, 'movies/movies_list.html', {"movies": movies})


def movies_list_signed_in(request):
    movies = Movie.objects.all().order_by('date')
    return render(request, 'movies/signed_in.html', {"movies": movies})


def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    # review = Review.objects.all().order_by('date')
    return render(request, 'movies/movies_detail.html', {"movie": movie})


def movie_detail_signed_in(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, 'movies/movies_detail_signed_in.html', {"movie": movie})


@login_required(login_url="/accounts/login/")
def create_review(request):
    if request.method == "POST":
        form = forms.CreateReview(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('movies:list')
    else:
        form = forms.CreateReview()
    return render(request, 'movies/create_review.html', {"form": form})
