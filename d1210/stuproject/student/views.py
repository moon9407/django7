from django.shortcuts import render,redirect
from .models import Student

# 학생등록함수
def write(request):
   if request.method == 'GET' :
      return render(request, 'student/write.html')
   elif request.method == 'POST':
      # form 에서 넘어온 데이터 처리
      name = request.POST.get("name")
      age = request.POST.get("age")
      grade = request.POST.get("grade")
      gender = request.POST.get("gender")
      qs = Student(name=name,age=age,grade=grade,gender=gender).save()

      print("이름 : ",request.POST.get("name"))

      
      return redirect('/student/list/')
      # return redirect('/')

# 학생리스트 함수
def list(request):
   # db명령어 qs로 지정
   qs = Student.objects.all()
   # qs2 = Student.objects.get(name='유관순')
   context = {"list":qs}
   return render(request, 'student/list.html',context)
