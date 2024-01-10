from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.api.Login.serializers import LoginSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
