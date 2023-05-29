
from django.urls import path
from music.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, UserUploadMusicView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('uploadmusic/', UserUploadMusicView.as_view(), name='uploadmusic'),
]