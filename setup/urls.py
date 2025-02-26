from django.contrib import admin
from django.urls import path, include
from . import views as views_setup # 'as' seria um apelido para aquele import
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exemplos-basico/', include("exemplos_basicos.urls")),
    path('interno/', include('interno.urls')),
    path('publico/', include('publico.urls')),
    path('', views_setup.home),
    path('login', auth_views.LoginView.as_view(template_name='clientes/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
