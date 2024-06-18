from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, email_verification, UserListView, toggle_activity, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('users_list/', UserListView.as_view(), name='view_all_users'),
    path('toggle_activity/<int:pk>/', toggle_activity, name='toggle_activity'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='view_user'),
]