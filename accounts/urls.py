from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),    
]


