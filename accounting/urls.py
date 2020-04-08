from django.urls import path

from . import views

app_name = 'accounting'
urlpatterns = [
    path('', views.index, name='index'),
    path('plants/', views.index, name='index'),
    path('plants/<int:plant_id>/', views.plant_detail, name='plant_detail'),
]
