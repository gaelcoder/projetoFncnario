from django.urls import path
from funcionarios import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'funcionarios'

urlpatterns = [
    #crud
    path('funcionario/<int:funcionariouni_id>/details/', views.funcionariouni, name='funcionariouni'),
    path('funcionario/create', views.funcionariouni, name='funcionariouni'),
    path('funcionario/<int:funcionariouni_id>/update/', views.funcionariouni, name='funcionariouni'),
    path('funcionario/<int:funcionariouni_id>/delete/', views.funcionariouni, name='funcionariouni'),

    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
