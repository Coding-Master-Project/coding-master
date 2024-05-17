from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from cmapp.models import Question

#질문 목록(메인)
def index(request):
    # request.session['user_id'] = request.user
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(answer__content__icontains=kw) | #답변 내용 검색
            Q(author__username__icontains=kw) | #질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10) #페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page':page, 'kw':kw}
    return render(request, 'cmapp/question_list.html', context)

#질문 상세
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    # 중복 방지를 위해 쿠키 설정
    session_cookie = request.COOKIES.get('sessionid') # 로그인할 때 생기는 sessionid 쿠키 받아오기
    print(session_cookie)
    cookie_name = F'question_views:{session_cookie}' # 쿠키 이름 설정, f-string 문자열 포맷팅 이용 
    response = render(request, 'cmapp/question_detail.html', context)

    if request.COOKIES.get(cookie_name) is not None: # 사용자가 글을 1개라도 조회했을 때
        cookies = request.COOKIES.get(cookie_name) # 현재 클라이언트의 쿠키 얻어오기
        cookies_list = cookies.split('|') # 파싱(question.id로 이루어진 list)
        if str(question_id) not in cookies_list: # 쿠키 리스트에 현재 question_id가 없으면 (= 조회수 중복이 아닌 경우)
            response.set_cookie(cookie_name, cookies + f'|{question_id}', expires=None) # 현재 쿠키들 뒤에 | 붙이고, question_id 쿠키 추가 (expires=None : 세션 쿠키 -> 브라우저(탭 말고 전체)를 종료할 때 쿠키 만료)
            question.views += 1 # 조회수 증가
            question.save() # 데이터베이스 변경 사항 저장
            return response
    else: # 사용자가 글을 아예 조회하지 않았을 때
        response.set_cookie(cookie_name, question_id, expires=None) # question_id 쿠키 설정
        question.views += 1 # 조회수 증가
        question.save() # 데이터베이스 변경 사항 저장
        return response

    return render(request, 'cmapp/question_detail.html', context)