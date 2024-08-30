from django.urls import path
from funcionarios import views

app_name = 'funcionarios'

urlpatterns = [
    path('', views.index, name='index')
]
