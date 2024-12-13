from django.urls import path
from django_app.api.user.auth.user import SignUpAPIView, LoginAPIView, LogoutAPIView
from django_app.api.user.follow.follower_and_following import FollowAPIView
from django_app.api.views import UserListAPIView
from django_app.api.elastic.user_search import UsernameSearch
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='account_signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

    # For Search User
    path('username-search/', UsernameSearch.as_view(), name='username_search'),

    # Follow/Unfollow
    path('follow/<int:id>/', FollowAPIView.as_view(), name='follow_unfollow'),

]


