from django.shortcuts import render
from django.http import JsonResponse
from member.models import Member

def step03(request):
    return render(request, 'member/step03.html')

# json 리턴 : 아이디 중복체크
def idCheck(request):
    #db에서 확인
    id = request.GET.get('id','')
    qs = Member.objects.filter(id=id)
    if not qs:
        result = '사용가능'
    else: result = '사용불가'
    
    #-------------------
    
    context = {'result' : '사용가능'}
    return JsonResponse(context)
