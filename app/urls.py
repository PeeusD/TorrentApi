
from django.urls import path
from app.views import TorrentHandlerView, UserregistrationView, UserLoginView, UserProfileView
urlpatterns = [
 
    path('torrent/', TorrentHandlerView.as_view() ),
    path('register/', UserregistrationView.as_view() , name='register'),
    path('login/', UserLoginView.as_view(), name='login' ),
    # path('profile/', UserProfileView.as_view() , name='profile'),
    
]
