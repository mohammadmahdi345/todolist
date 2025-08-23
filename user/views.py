from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
import logging

#logger = logging.getLogger('jwt_debug')

from user.serializers import UserSerializer , LoginSerializer, UserGetSerializer


class RegisterView(APIView):

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'detail': 'register successful',
                             'access_token': access_token,
                             'refresh_token': str(refresh)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(username=username, email=email)
            except User.DoesNotExist:
                return Response({'detail': 'User not found'}, status=404)

            if not user.check_password(password):
                return Response({'detail': 'Incorrect password'}, status=400)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            #logger.info(f'token login === {access_token}')
            return Response({
                'detail': 'login successful',
                'access_token': access_token,
                'refresh_token': str(refresh)
            }, status=200)


        return Response(serializer.errors, status=400)


class UserGetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        users = User.objects.all()
        serializer = UserGetSerializer(users,many=True)
        return Response(serializer.data,status=200)


class UserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        serializer = UserGetSerializer(user)
        return Response(serializer.data,status=200)