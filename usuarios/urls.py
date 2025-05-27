from django.urls import path, include
from .views import home, registrar_usuario, acceder
from rest_framework import routers
from django.contrib.auth.views import LogoutView
from usuarios.views import UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('logout/', LogoutView.as_view(next_page='acceder'), name='logout'),
    path('registro/', registrar_usuario, name='registro'),
    path('acceder/', acceder, name='acceder'),
    
    path('api/', include(router.urls))
]
