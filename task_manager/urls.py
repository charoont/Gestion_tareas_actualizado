from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tareas.views import TareaViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

