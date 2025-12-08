from django.urls import path,include
from . import views

app_name = 'std'
urlpatterns = [
    path('write/', views.write, name='write'),
]
