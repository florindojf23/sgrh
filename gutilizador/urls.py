from django.urls import path
from . import views
from . import views_controlo
urlpatterns = [
	path('profile/', views.ProfileUpdate, name="user-profile"),
	path('profile/image-update/', views.ProfileImageUpdate, name="user-profile-image-update"),
	path('my/account/', views.AccountUpdate, name='user-account'),
	path('change/password/', views.UserPasswordChangeView.as_view(), name='user-change-password'),
	path('change/password/done/', views.UserPasswordChangeDoneView.as_view(), name='user-change-password-done'),

	path('my/account/login/history/', views.AccountLoginHistory, name='user-login-history'),

	
	path('ativu-user/<str:id>', views.ativuUser, name="ativuUser"),
	path('desativu-user/<str:id>', views.desativuUser, name="desativuUser"),
	path('reset-user-password/<str:id>', views.resetUserPassword, name="resetUserPassword"),

	path('list/', views.UserList, name="userlist"),
	path('list/group/<str:id>', views.user_with_group, name="user_with_group"),
	path('create/', views.createUser, name="createUser"),
	path('funcionario/create/', views.createUserFuncionario, name="createUserFuncionario"),

	# controlo gestoes
	path('controlo-de-gestoes/', views_controlo.controlo_gestoes, name='controlo-gestoes'),
	
	path('search-funcionario/', views.search_funcionario, name='search_funcionario'),
	
]