from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tareas.views import TareaViewSet

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración del esquema de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Trello API",
        default_version='v1',
        description="Documentación de la API de tareas estilo Trello",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Rutas API
router = DefaultRouter()
router.register(r'tareas', TareaViewSet)

# URLs
urlpatterns = [
    path('', include(router.urls)),  
    path('admin/', admin.site.urls), 
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger
]

