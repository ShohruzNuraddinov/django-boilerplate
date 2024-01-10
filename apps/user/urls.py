from django.urls import path

from apps.user.api.Login.views import LoginView
from apps.user.api.Register.views import RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
