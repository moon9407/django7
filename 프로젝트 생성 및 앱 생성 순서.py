# 기본 cmd 순서
# cd..     : 상위 폴더로 접속,      cls : cmd 화면 지우기

### 1.주소 지정----------------------------------------------------------------------------
# cd C:\workspace\django7\d1208(주소) : 해당 주소 폴더위치 접속

### 2. 장고 프로젝트 생성 및 실행-------------------------------------------------------------
# django-admin startproject stupjt01(프로젝트명) : 장고 프로젝트 생성
# python manage.py runserver : 장고 서버 실행 되는지 확인 후 닫기
##### 서버 시작은 cmd창에서 하기(오류 생길 수 있음)

### 3. 장고 앱 생성 및 설정------------------------------------------------------------------
# python manage.py startapp student(앱이름) : 장고 앱 생성
# 프로젝트에 가서 setting.py 에서 INSTALLED_APPS에 앱 이름 추가 후
# LANGUAGE_CODE = 'ko-kr'
# TIME_ZONE = 'Asia/Seoul'
# 상단에 import os 추가
# # 정적 파일 위치 지정 - 정적파일 종류 : css, js, image 
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
# ]
# 설정 후 저장
# 프로젝트(메인) 파일에 static 폴더 생성 후 그 안에 css, js, images 폴더 생성

### 4. 프로젝트 urls.py 설정 및 뷰 작성-------------------------------------------------------
# 프로젝트 urls.py에서 필요 없는 부분(맨위 ''' 내용, ) 제거 후  from django.urls import path,include 로 수정
# urlpatterns 부분에 path('student/', include('student.urls')), 한줄 추가

### 5. 생성한 앱 urls.py 작성----------------------------------------------------------------
# student 폴더에 urls.py 파일 생성 후 stupjt01의 urls.py 내용 복붙 후 admin 부분 제거
# 상단에 from . import views 추가
# app_name ='student' 추가
# urlpatterns에 path('write/', views.write, name='write'), 추가
# student 폴더의 views.py에서 write 함수 생성
# def write(request):
#    return render(request, 'write.html')

### 6. templates 폴더 생성 및 작성----------------------------------------------------------------
# student 폴더에 templates 폴더 생성 후  그 안에 write.html 파일 생성
# write.html 에 기본 html 작성
# h2 태그 만들고 내용 넣기

### 7. 서버 실행 및 접속 확인 -----------------------------------------------------------------
# python manage.py runserver 로 서버 실행
# http://127.0.0.1:8000/student/write/ 접속 확인 

### 8. home 앱 생성---------------------------------------------
# python manage.py startapp home(앱이름) : 앱 생성
# setting.py 에서 installed_apps에 'home', 추가

### 9. 프로젝트 urls.py 설정 및 뷰 작성-------------------------------------------------------
# 프로젝트 urls.py 에서 path('', include('home.urls')), 추가
# home 폴더에 urls.py 파일 생성 후 아래 내용 작성
# from django.urls import path,include
# from . import views

# app_name = ''
# urlpatterns = [
#     path('', views.index, name= 'index'),
# ]

# views.py 에서 
# def write(request):
#     return render(request, 'index.html')
# 입력

### 10. templates 폴더 생성 및 작성----------------------------------------------------------------
# home 폴더에 templates 폴더 생성 후 그 안에 index.html 파일 생성
# index.html 에 기본 html 작성

### 11. 서버 실행 및 접속 확인 -----------------------------------------------------------------
# python manage.py runserver 로 서버 실행
# http://127.0.0.1:8000/ 접속 확인

### a태그 넣는 법---------------------------
# <a href = "/student/write"></a>  : 메인에서 이동할 페이지 설정
# <a href = "/"></a>  : 다른페이지에서 메인페이지로 이동


#-----------------------------------------------------
# cmd창에서 ctrl+c 입력 시 서버종료
