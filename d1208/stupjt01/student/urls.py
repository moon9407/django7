from django.urls import path,include
from . import views

# app_name : 닉네임
app_name ='student'
urlpatterns = [
    # write 페이지 url로 들어와서 write함수  호출
    path('write/', views.write, name='write'),
]


