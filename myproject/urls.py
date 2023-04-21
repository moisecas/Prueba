
from django.urls import path
from . import views

urlpatterns = [
    # Endpoints para el manejo de usuarios
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('users/<int:pk>/sessions/', views.UserSessionListAPIView.as_view(), name='user-session-list'),
    
    # Endpoints para el manejo de sesiones
    path('sessions/', views.SessionListCreateAPIView.as_view(), name='session-list-create'),
    path('sessions/<int:pk>/', views.SessionRetrieveAPIView.as_view(), name='session-detail'),
    path('sessions/<int:pk>/clicks/', views.SessionClickListAPIView.as_view(), name='session-click-list'),
    
    # Endpoints para el manejo de landing page
    path('landing-page/', views.LandingPageCreateAPIView.as_view(), name='landing-page-create'),
    path('landing-page/<int:pk>/', views.LandingPageRetrieveUpdateAPIView.as_view(), name='landing-page-detail'),
]

