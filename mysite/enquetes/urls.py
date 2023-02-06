from django.urls import path
from .views import *
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('cadastrar_usuario/', cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario/', logar_usuario, name="logar_usuario")
]