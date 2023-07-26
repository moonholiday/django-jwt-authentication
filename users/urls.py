from django.urls import path
from .views import HomePageView, UserRegistrationView, UserLoginView, LoginView, SignupView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('api/signup/', UserRegistrationView.as_view(), name='signup-api'),
    path('api/login/', UserLoginView.as_view(), name='login-api'),
]
