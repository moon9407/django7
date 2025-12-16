from django.shortcuts import render,redirect
from .models import Board
import datetime

# 게시글 작성
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bfile = request.FILES.get('bfile')  # file타입이기에 FILES 로 읽어야 함.
        # 파일명 중복 방지용으로 앞에 시간 붙이기
        # bfile = f'{datetime.datetime.now().microsecond}_{bfile}' 
        print('post btitle 정보 : ',btitle)
        print('post bfile 정보 : ',bfile)
        print("날짜 : ",datetime.datetime.now())
        print("날짜 : ",datetime.datetime.now().microsecond)
        
        # 파일 저장
        qs = Board(btitle=btitle,bfile=bfile)
        qs.save()

        return render(request,'board/write.html')
        
