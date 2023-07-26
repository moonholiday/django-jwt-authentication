from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer, UserLoginSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Signup successful.'}, status=status.HTTP_201_CREATED)
        else:
            error_data = serializer.errors
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class HomePageView(TemplateView):
    template_name = "base.html"


class SignupView(TemplateView):
    template_name = 'frontend_signup.html'


class LoginView(TemplateView):
    template_name = 'frontend_login.html'
