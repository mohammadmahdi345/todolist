from django.urls import path, include


from .views import RegisterView, LoginView, UserView,UserGetView


urlpatterns = [

    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', UserGetView.as_view()),
    path('user/', UserView.as_view())
    ]