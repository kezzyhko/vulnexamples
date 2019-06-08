from django.urls import path

from . import views


app_name = 'a9_cve'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
