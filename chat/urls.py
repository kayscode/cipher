from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="chat_index"),
    path('login/', views.login, name="chat_login"),
    path('signup/', views.signup, name="chat_signup"),
    path('logout/', views.index, name="chat_logout")
]
