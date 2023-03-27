from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="chat_index"),
    path('login/', views.login, name="chat_login"),
    path('signup/', views.signup, name="chat_signup"),
    path('logout/', views.index, name="chat_logout"),
    path('signup/failed',TemplateView.as_view(template_name="chat/auth/signup_failed.html"),name="password_failed_message"),
    path('discussions/', views.discussions_index, name="discussions_index")
]
