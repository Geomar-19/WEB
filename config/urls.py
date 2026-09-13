from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from recursos import views # Importamos las vistas de nuestra app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('descargar/<int:recurso_id>/', views.descargar_recurso, name='descargar_recurso'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)