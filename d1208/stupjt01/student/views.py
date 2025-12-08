from django.shortcuts import render

# write 함수 생성 : 성적입력 페이지 열기
def write(request):
    return render(request, 'write.html')
