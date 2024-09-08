from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, registro, perfil, actualizar

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', registro, name='registro'),
    
    path('', index, name='index'),
    path('profile/', perfil, name='perfil'),
    path('update/', actualizar, name='actualizar'),
    
]