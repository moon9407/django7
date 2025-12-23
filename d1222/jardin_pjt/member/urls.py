from django.urls import path,include
from . import views

app_name = 'member'
urlpatterns = [
    # html 리턴
    path('step03/', views.step03, name='step03'),
    # json 리턴 : 아이디 중복체크
    path('idCheck/', views.idCheck, name='idCheck'),
]

