"""
URL configuration for hrms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from master.views import loginPage,logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/sgrh/', admin.site.urls),
    path('login/', loginPage, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include('master.urls')),
    path('gutilizador/', include('gutilizador.urls')),
    path('gfuncionarios/', include('gfuncionarios.urls')),
    path('gdivisao_administrativa/', include('gdivisao_administrativa.urls')),
    path('gcarreira/', include('gcarreira.urls')),
    path('funcao/', include('funcao.urls')),
    path('gavaliacao_desempenho/', include('gavaliacao_desempenho.urls')),
    path('ministerio/', include('unidade_ministerio.urls')),
    path('reports/', include('reports.urls')),
    path('habilitacao/', include('habilitacao.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "SGRH-ME - Sistema Gestao Recursos Humanos-ME - SUPER USER"
admin.site.site_title = "SGRH-ME - Sistema Gestao Recursos Humanos-ME - SUPER USER"
admin.site.index_title = "Pajina Super User"
