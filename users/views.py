from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .models import CustomUser, profile
from .serializers import CustomUserSerializer, ProfileSerializer, LoginSerializer,RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class RegisterView(generics.CreateAPIView):
 
    permission_classes = [AllowAny]

    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user).data,
            "profile": ProfileSerializer(user.profile).data  
        })

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user:
                return Response({
                    'user_id': user.user_id, 
                    'message': "User authenticated successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'detail': 'User authentication failed.'
                }, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer


