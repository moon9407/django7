from django.shortcuts import render, redirect
from .models import Student

# 학생등록함수
def write(request):
    if request.method == 'GET':
        return render(request, 'student/write.html')
    elif request.method == 'POST':
        # form폼에서 넘어온 데이터 처리
        name = request.POST.get("name")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        # hobbys = ','.join(hobby)  # 리스트 타입을 문자열 타입으로 변환방법
        # 리스트타입을 문자열항목에 저장하면 자동으로 형변환됨.
        Student(name=name, age=age, grade=grade, gender=gender,hobby=hobby).save()
        # qs.save()
        
        # Student.objects.create(name=name, age=age, grade=grade, gender=gender)

        
        print("이름 : ", name)
        print("취미 : ", hobby)
        return render(request, 'student/write.html')
        # return redirect('/student/list/')
    

    #return redirect('/')

# 학생리스트함수
def list(request):
    # DB에서 전체 레코드 가져오기
    # select, insert, update, delete
    
    qs = Student.objects.all()
    
    # qs = Student.objects.get(name="홍길동")
    # qs2 = Student.objects.get(name="유관순")
    
    # context = {"name":"홍길자","student":qs, "student2":qs2}
    
    context = {"list":qs}

    
    return render(request, 'student/list.html', context)

# 학생리스트함수
def view(request):
    return render(request, 'student/list.html')

# 학생리스트함수
def delete(request):
    return render(request, 'student/list.html')
