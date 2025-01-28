from django.urls import path
from master.views import *

urlpatterns = [
	path('',index,name='home'),
	path('configuracao-de-sistema/',Configuracaosystema,name='configuracao-sistema'),



	path('ajax/load-posts/', load_posts, name='ajax_load_posts'),
    path('ajax/load-villages/', load_villages, name='ajax_load_villages'),
    path('ajax/load-aldeias/', load_aldeias, name='ajax_load_aldeias'),
    
    path('ajax/load-dir-nac/', load_dir_nac, name='ajax_load_dir_nac'),
    
    path('ajax/load-escola-dg/', load_escola_dg, name='ajax_load_escola_dg'),
    
    path('ajax/load-dir-geral-sec-estado/', load_dir_geral, name='ajax_load_dir_geral'),
    path('ajax/load-departamento/', load_departamento, name='ajax_load_departamento'),
    path('ajax/load-seccao/', load_seccao, name='ajax_load_seccao'),
]