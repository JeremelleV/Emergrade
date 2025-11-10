from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="core-main"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name='signup'),  # Add this line
    path('signin/', views.signin, name='signin'),  # Add this line
    path('signout/', views.signout, name='signout'),
    ]
