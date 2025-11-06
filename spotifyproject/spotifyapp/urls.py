import debug_toolbar
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import register_view, songs_view, like_songs_view, add_to_like_songs, remove_to_like_songs

urlpatterns = [
    path('LikeSongs/', like_songs_view, name='like_songs_view'),
    path('LikeSongs/add_like/<int:song_id>/',add_to_like_songs, name='add_to_like_songs'),
    path('LikeSongs/remove_like/<int:song_id>/',remove_to_like_songs, name='remove_to_like_songs'),
    path('', songs_view, name='songs'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path("__debug__/", include("debug_toolbar.urls")),
    ]