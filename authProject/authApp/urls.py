from django.urls import path
from . import views

# URL patterns
urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
]
