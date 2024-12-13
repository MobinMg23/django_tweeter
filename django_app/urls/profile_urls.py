from django.urls import path
from django_app.api.user.profile.profile_api import ProfileCreate, EditeProfile


urlpatterns = [
    path('profile-create/', ProfileCreate.as_view(), name='profile-create'),
    path('profile-edite/', EditeProfile.as_view(), name='profile-edite'),
]