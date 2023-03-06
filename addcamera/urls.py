
from django.contrib import admin
from django.urls import path, include
from addcamera import views
urlpatterns = [
    path('', views.add_camera, name='add_camera'),
    path('signup', views.SignUp, name='signup'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('book/<email>/<username>', views.Book, name='book'),
    path('feedback', views.Feedback, name='feedback'),
    path('main', views.Main, name='main'),

]
