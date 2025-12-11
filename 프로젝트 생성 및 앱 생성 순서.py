# python 주석
# <!-- html 주석 -->
# {% comment %} django주석 {% endcomment %}

# 기본 cmd 순서
# cd..     : 상위 폴더로 접속,      cls : cmd 화면 지우기
#=================================================================================================
### 1.주소 지정
# cd C:\workspace\django7\d1208(주소) : 해당 주소 폴더위치 접속

### 2. 장고 프로젝트 생성 및 실행
# django-admin startproject stupjt01(프로젝트명) : 장고 프로젝트 생성
# python manage.py runserver : 장고 서버 실행 되는지 확인 후 닫기
##### 서버 시작은 cmd창에서 하기(오류 생길 수 있음)

### 3. 장고 앱 생성 및 설정
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

### 4. 프로젝트 urls.py 설정 및 뷰 작성
# 프로젝트 urls.py에서 필요 없는 부분(맨위 ''' 내용, ) 제거 후  from django.urls import path,include 로 수정
# urlpatterns 부분에 path('student/', include('student.urls')), 한줄 추가

### 5. 생성한 앱 urls.py 작성
# student 폴더에 urls.py 파일 생성 후 stupjt01의 urls.py 내용 복붙 후 admin 부분 제거
# 상단에 from . import views 추가
# app_name ='student' 추가
# urlpatterns에 path('write/', views.write, name='write'), 추가
# student 폴더의 views.py에서 write 함수 생성
# def write(request):
#    return render(request, 'write.html')

### 6. templates 폴더 생성 및 작성
# student 폴더에 templates 폴더 생성 후  그 안에 write.html 파일 생성
# write.html 에 기본 html 작성
# h2 태그 만들고 내용 넣기

### 7. 서버 실행 및 접속 확인
# python manage.py runserver 로 서버 실행
# http://127.0.0.1:8000/student/write/ 접속 확인 

### 8. home 앱 생성
# python manage.py startapp home(앱이름) : 앱 생성
# setting.py 에서 installed_apps에 'home', 추가

### 9. 프로젝트 urls.py 설정 및 뷰 작성
# 프로젝트 urls.py 에서 path('', include('home.urls')), 추가
# home 폴더에 urls.py 파일 생성 후 아래 내용 작성
# from django.urls import path,include
# from . import views

# app_name = ''
# urlpatterns = [
#     path('', views.index, name= 'index'),
# ]

# views.py 에서 
# def index(request):
#     return render(request, 'index.html')
# 입력

### 10. templates 폴더 생성 및 작성
# home 폴더에 templates 폴더 생성 후 그 안에 index.html 파일 생성
# index.html 에 기본 html 작성

### 11. 서버 실행 및 접속 확인
# python manage.py runserver 로 서버 실행
# http://127.0.0.1:8000/ 접속 확인

### a태그 넣는 법
# <a href = "/student/write"></a>  : 메인에서 이동할 페이지 설정
# <a href = "/"></a>  : 다른페이지에서 메인페이지로 이동


# cmd창에서 ctrl+c 입력 시 서버종료


#=================================================================================================
#### db 생성
# student폴더의 models.py에서 
# class Student(models.Model):      # class 이름(models.Model)
#     sno = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100) 
#     age = models.IntegerField(default=0)
#     grade = models.IntegerField(default=1)
#     gender = models.CharField(max_length=10)
    
#     def __str__(self):
#         return f"{self.sno},{self.name},{self.age},{self.grade},{self.gender}"
# 입력 후 저장

### admin 생성
# student 폴더의 admin.py에서 상단에 from student.models import Student 후
# admin.site.register(Student) 입력  후 저장
# 터미널 창에서 python manage.py makemigrations 입력 후 엔터
# python manage.py migrate 입력 후 엔터 : ok 나오면 생성완료

### admin 관리자 등록
# python manage.py createsuperuser 입력 후 엔터
# username : admin 입력 후 엔터
# email address : admin@naver.com 입력 후 엔터
# password : 1111 입력 후 엔터 (보안상 화면에 안나옴)
# password(again) : 1111 입력 후 엔터
# - 패스워드 사용여부 확인[Y/N] : y 입력 후 엔터

###  생성된 db확인 방법과 롤백 방법---------------------------------------
# 터미널 창에 python manage.py showmigrations : 생성된 db확인 방법
# python manage.py migrate <app_name> zero : 롤백
#=================================================================================================
###  db 명령어
## python manage.py shell 로 db 접속
# from student.models import Student 후
# 원하는 명령어 입력
## 1. insert : 데이터 저장
# qs = Student(sno=1, name='홍길동', age=20, grade='2',gender='남자')
# qs.save()      # 저장

## 2. select : 데이터 조회
# Student.objects.all() : 전체조회
# Student.objects.get(id='aaa') : 단일조회
# Student.objects.filter(age=20) : 여러개 조회
# Student.objects.filter(name__contains='순') : 포함되어 있는지 검색
## 시작,끝 부분에 있는 것 검색 : _ _startswith, _ _ endwith
# Student.objects.filter(name__startswith='홍')
## 크다,작다,크거나같다,작거나같다 비교 검색 : gt,gte,lt,lte
# Student.objects.filter(age__gte=21)
## 특정 컬럼만 조회
# Student.objects.values('name')
## 정렬
# Student.objects.order_by('age') : age 앞에 - 붙이면 역순
## * 파일 존재 확인 :  exists()
# Member.objects.filter(age=50).exists()

## 3.update : 데이터 수정
# qs = Student.objects.get(id='aaa') : 원하는 데이터 선택 후
# qs.name = '홍길스' : 수정 데이터 입력
# qs.age = 50 : 수정 데이터 입력
# qs.save()     : 수정 데이터 저장

## 4. delete : 데이터 삭제
# qs = Student.objects.get(id='aaa') : 원하는 데이터 선택 후
# qs.delete() : 삭제

## db명령어 종료
# exit() 로 나가기

#=================================================================================================
### 값 가져오는 방법
# 해당 앱의 views.py 에서 
# def list(request):
#    # db명령어 qs로 지정
#    qs = Student.objects.all()
#    # qs2 = Student.objects.get(name='유관순')
#    context = {"list":qs}
#    return render(request, 'student/list.html',context)
# 로 변경
# 해당 html에서 원하는 위치에 {{"student"}} 로 해당 값 가져오기

#=================================================================================================
### django html 문법-------------------------------------------------------
# for문, if문, 변수 사용가능
## for문
# {% for s in list %}            # 시작
    # <tr>
    #     <td>{{s.sno}}</td>
    #     <td>{{s.name}}</td>
    #     <td>{{s.age}}</td>
    #     <td>{{s.grade}}</td>
    #     <td>{{s.gender}}</td>
    # </tr>
# {% endfor %}                   # 끝

## if문
# {% if list %}                  #시작
# {% for s in list %}
    # <tr>
    #     <td>{{s.sno}}</td>
    #     <td>{{s.name}}</td>
    #     <td>{{s.age}}</td>
    #     <td>{{s.grade}}</td>
    #     <td>{{s.gender}}</td>
    # </tr>
# {% else %}                     # 중간
    # <tr>
    #     <td colspan='5'>데이터가 존재하지 않습니다.</td>
    # </tr>
# {% endif %}                    # 끝

#===================================================================================================
## {% csrf_token %} : 보안토큰으로 해킹방지용
## {% url "student:write" %} : 상대경로
## /student/list : 절대경로

#===================================================================================================
# 링크 방식
# 1) 앱이름 url방식
# {% url "student:view" s.sno s.name %}
# 2) rest api url방식
# /student/{{s.sno}}/view/
# 3) 파라미터 방식
# /student/view?sno={{s.sno}}&name={{s.name}}

