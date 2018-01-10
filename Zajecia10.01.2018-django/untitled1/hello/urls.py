from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)/', views.calc, name='calc'),
    url(r'^$', views.index, name='index')
]