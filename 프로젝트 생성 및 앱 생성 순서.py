# 기본 cmd 순서
# cd..     : 폴더 위치 접속,      cls : cmd 화면 지우기

## 1.주소 지정--------------------------------------------------------------------------
# cd 주소 : 해당 주소 폴더위치 접속
## 2. 장고 프로젝트 생성 및 실행---------------------------------------------------------
# django-admin startproject 프로젝트명 : 장고 프로젝트 생성
# python manage.py runserver : 장고 서버 실행 되는지 확인 후 닫기 (나중에 해도 상관없음)
## 3. 장고 앱 생성 및 설정------------------------------------------------------------------
# python manage.py startapp student#앱이름 : 장고 앱 생성
# 프로젝트에 가서 setting.py 에서 INSTALLED_APPS에 앱 이름 추가
# 4. 프로젝트 urls.py 설정 및 뷰 작성-------------------------------------------------------
# urls.py에서 필요 없는 부분(맨위 ''' 내용, ) 제거 후  from django.urls import path,include 로 수정
# urlpatterns에 path('student/', include('student.urls')), 한줄 추가
# 5. 생성한 앱 urls.py 작성----------------------------------------------------------------
# student 폴더에 urls.py 파일 생성 후 stupjt01의 urls.py 내용 복붙 후 admin 부분 제거
# from . import views 추가
# app_name ='student' 추가
# urlpatterns에 path('write/', views.write, name='write'), 추가
# student 폴더의 views.py에서 write 함수 생성
# def write(request):
#    return render(request, 'write.html')
# 6. 템플릿 폴더 생성 및 작성----------------------------------------------------------------
# student 폴더에 templates 폴더 생성 후  그 안에 write.html 파일 생성
# h2 태그에 내용 넣기
# 7. 서버 실행 및 접속 확인 ------------------------------------------------------------------
# python manage.py runserver 로 서버 실행
# http://127.0.0.1:8000/student/write/ 접속 확인 




# cmd창에서 ctrl+c 입력 시 서버종료
