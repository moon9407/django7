from django.shortcuts import render,redirect
from board.models import Board
from member.models import Member
from django.db.models import F, Q

# 게시판 답글달기
def reply(request, bno):
    if request.method == 'GET':
        # 원글 가져오기
        board = Board.objects.get(bno=bno)
        context = {'board': board}
        return render(request, 'board/reply.html', context)
    elif request.method == 'POST':
        # 원글 정보 가져오기
        parent_board = Board.objects.get(bno=bno)
        
        # 같은 그룹의 다음 순서부터 step 증가
        Board.objects.filter(bgroup=parent_board.bgroup, bstep__gt=parent_board.bstep).update(bstep=F('bstep')+1)
        
        # 세션에서 로그인 정보 가져오기
        id = request.session.get('session_id')
        member = Member.objects.get(id=id)
        
        # 답글 데이터 가져오기
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile', '')
        
        # 답글 저장
        Board.objects.create(
            member=member,
            btitle=btitle,
            bcontent=bcontent,
            bfile=bfile,
            bgroup=parent_board.bgroup,
            bstep=parent_board.bstep + 1,
            bindent=parent_board.bindent + 1
        )
        
        return redirect('board:list')

# 게시판 수정
def update(request, bno):
    # 로그인 체크
    if not request.session.get('session_id'):
        return redirect('/member/login/')
    
    # 게시글 가져오기
    board = Board.objects.get(bno=bno)
    
    # 작성자 본인 확인
    if board.member.id != request.session.get('session_id'):
        return redirect('board:view', bno=bno)
    
    if request.method == 'GET':
        # 수정할 게시글 가져오기
        context = {'board': board}
        return render(request, 'board/update.html', context)
    
    elif request.method == 'POST':
        # 게시글 수정
        board.btitle = request.POST.get('btitle')
        board.bcontent = request.POST.get('bcontent')
        if 'bfile' in request.FILES:
            board.bfile = request.FILES.get('bfile')
        board.save()
        return redirect('board:view', bno=bno)

# 게시판 삭제
def delete(request,bno):
    # 로그인 체크
    if not request.session.get('session_id'):
        return redirect('/member/login/')
    
    # 게시글 가져오기
    board = Board.objects.get(bno=bno)
    
    # 작성자 본인 확인
    if board.member.id != request.session.get('session_id'):
        return redirect('board:view', bno=bno)
    
    board.delete()
    return redirect("/board/list/")

# 게시판 상세보기
def view(request,bno):
    # 게시글 가져오기
    # 조회를 한후 조회된 데이터들을 update를 통해 bhit 1증가
    Board.objects.filter(bno=bno).update(bhit = F('bhit') + 1)
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view.html',context)

from django.core.paginator import Paginator


# 게시판 리스트
def list(request):
    # 게시글 모두 가져오기
    qs = Board.objects.all().order_by('-bgroup','bstep')
    # 하단 넘버링 (qs,10) -> 
    paginator = Paginator(qs, 10)
    page = int(request.GET.get('page',1))
    list_qs = paginator.get_page(page) # 1page -> 게시글 10개를 전달
    
    context = {'list':list_qs,'page':page}
    return render(request,'board/list.html',context)

# 게시판 글쓰기
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        id = request.session.get('session_id')
        member_qs = Member.objects.get(id=id)
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')
        # bgroup 값을 입력
        qs = Board.objects.create(btitle=btitle,bcontent=bcontent,member=member_qs,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'flag':'1'}
        return render(request,'board/write.html',context)
        