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
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile_data = {
                'profile_id': user,
                'height': serializer.validated_data.get('height'),
                'weight': serializer.validated_data.get('weight'),
                'location': serializer.validated_data.get('location'),

            }
            profile = user.profile  
            profile_serializer = ProfileSerializer(profile)
            return Response({
                'user': serializer.data,
                'profile': profile_serializer.data,
                'message': "User authenticated successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']

        return Response({
                'user_id': user.user_id,
                'message': "User authenticated successfully"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer


