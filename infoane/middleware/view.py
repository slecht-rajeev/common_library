import logging
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken as SimpleJWTRefreshToken

from .models import AccessControl
from .serializers import LoginSerializer, AccessSerializer

logger = logging.getLogger(__name__)


class RefreshToken(SimpleJWTRefreshToken):
    @classmethod
    def for_user(cls, user):
        token = cls()
        token['user_id'] = user.id
        return token

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            try:
                queryset = AccessControl.objects.get(user_admin=user.id)
                serializer_access = AccessSerializer(queryset)
                access_control=serializer_access.data
            except:
                access_control = {}

            return Response({
                'access_control': access_control,
                'username': user.username,
                'email_id': user.email_id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'detail': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            logout(request)  # Logs out the user from Django session

            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklists the refresh token if blacklist feature is enabled

            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class RefreshTokenAPIView(generics.GenericAPIView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({
                'access': serializer.validated_data['access'],
                'refresh': serializer.validated_data['refresh']
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)