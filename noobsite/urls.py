# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('index/error', views.index_view_error),
    path('index/wow', views.index_view_wow),
    path('index/msg', views.index_view_msg),
]