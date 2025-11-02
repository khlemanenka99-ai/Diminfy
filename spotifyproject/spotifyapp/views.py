from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Genre, Song, Album


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # хэшируем пароль
            user.save()
            login(request, user)  # сразу авторизуем пользователя
            return redirect('songs')  # редирект на список товаров
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def songs_view(request):
    genres = Genre.objects.all()
    genre_id = request.GET.get('genre')
    query = request.GET.get('q')
    songs = Song.objects.all()
    if genre_id:
        songs = songs.filter(genre_id=genre_id)
    if query:
        songs = songs.filter(
            Q(title__icontains=query) |
            Q(artist__name__icontains=query)
        )
    return render(request, 'songs.html', {
        'songs': songs,
        'genres': genres,
        'selected_genre': genre_id,
    })
