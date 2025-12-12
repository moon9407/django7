from django.shortcuts import render,redirect

def login(request):
    if request.method == 'GET':
        # 쿠키검색
        cooksave_id = request.COOKIES.get('cooksave_id',"")
        context = {"cooksave_id":cooksave_id}        
        return render(request, 'member/login.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        login_keep = request.POST.get('login_keep')
        # 쿠키 읽기
        print("모든쿠키 읽어오기",request.COOKIES)
        # 쿠키저장
        response = redirect("/")
        if login_keep:
            print("쿠키 저장.")
            ## 쿠키에 아이디를 저장시켜줌
            response.set_cookie('cooksave_id', id, max_age=60*60*24*30)
        else:
            print("쿠키 삭제.")
            response.delete_cookie('cooksave_id')
        print("POST 입력된 값 : ",id,pw,login_keep)
        
        return response
        