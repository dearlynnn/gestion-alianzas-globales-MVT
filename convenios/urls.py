from django.urls import path, include
from . import views
from .views import EmpresaViewSet, ConvenioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/empresas', EmpresaViewSet, basename='empresa')
router.register(r'api/convenios', ConvenioViewSet, basename='convenio')

urlpatterns = [
    path('listado/', views.lista_empresas, name='lista_empresas'),
    path('añadir/', views.crear_empresa, name='crear_empresa'),
    path('<int:empresa_id>/modificar/', views.editar_empresa, name='editar_empresa'),
    path('<int:empresa_id>/borrar/', views.eliminar_empresa, name='eliminar_empresa'),

    path('lista/', views.lista_convenios, name='lista_convenios'),
    path('crear/', views.crear_convenio, name='crear_convenio'),
    path('<int:convenio_id>/editar/', views.editar_convenio, name='editar_convenio'),
    path('<int:convenio_id>/eliminar/', views.eliminar_convenio, name='eliminar_convenio'),

    path('api/', include(router.urls))
]


urlpatterns += router.urls
