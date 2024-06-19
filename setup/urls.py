from django.contrib import admin
from django.urls import path, include
from . import views as views_setup # 'as' seria um apelido para aquele import


urlpatterns = [
    path('admin/', admin.site.urls),
    path('exemplos-basicos', include("exemplos_basicos.urls")),
    path('interno', include('interno.urls')),
    path('', views_setup.home),
]
