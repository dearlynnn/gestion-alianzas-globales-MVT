from django.urls import path, include
from .views import ProyectoViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/proyectos', ProyectoViewSet, basename='proyecto')

urlpatterns = [
    path('registrar/', views.registrar_proyecto, name='registrar_proyecto'),
    path('lista/', views.lista_proyectos, name='lista_proyectos'),
    path('<int:proyecto_id>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('<int:proyecto_id>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('detalles/<int:empresa_id>/', views.detalle_empresa, name='detalle_empresa'),

    path('api/', include(router.urls))
]

urlpatterns += router.urls