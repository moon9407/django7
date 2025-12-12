from django.shortcuts import render

def index(request):
    # 쿠키 검색 - request
    # 쿠키 저장 - response
    
    # 쿠키 검색
    cook_info = request.COOKIES
    print("쿠키모든정보 : ",cook_info)
    cook_id = request.COOKIES.get('cook_id', '') # 쿠키 정보 있을 때 가져오고 없으면 빈공백 처리
    print("cook_id 정보 : ",cook_id)

    ## 쿠키저장
    response = render(request, 'index.html')
    
    # 유지시간이 지정되지 않으면 브라우저 종료 시 삭제, 시간을 설정하면 그 시간동안 유지
    # if not cook_id:    
    #     response.set_cookie("smsite_connect", "ok") # ex) cook_id = aaa 와 같은말
    #     response.set_cookie("ip", "127.0.0.1:8000", max_age=60*60*24)  # 60초*60분*24시간*365일 = 1년 으로 계산

    
    return response
    
    
    
    
    return render(request, 'index.html')
