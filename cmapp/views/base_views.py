from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from cmapp.models import Question, Comment, PLanguage

#홈(메인 index)
def index(request):
    return render(request, 'html/Home/home.html')

#질문 목록
def list(request, planguage_id):
    print(planguage_id)
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #검색어
    type = request.GET.get('type', 'search-title') #검색 타입

    if planguage_id == 0 :
        question_list = Question.objects.order_by('-create_date')
    else :
        planguage = PLanguage.objects.filter(id=planguage_id).first()

        if planguage:
            question_list = Question.objects.filter(planguage=planguage).order_by('-create_date')

    if kw:
        if type == 'search-title': #제목 검색
            question_list = question_list.filter(
                Q(subject__icontains=kw) 
            )
        elif type == 'search-content': #내용 검색
            question_list = question_list.filter(
                Q(content__icontains=kw) 
            )
        elif type == 'search-t+c': #제목+내용 검색
            question_list = question_list.filter(
                Q(subject__icontains=kw) | #제목
                Q(content__icontains=kw) #내용
            ).distinct() #distinct는 중복 처리

    paginator = Paginator(question_list, 10) #페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    planguage_list = PLanguage.objects.all()
    context = {'question_list': page_obj,
                'page': page,
                'kw': kw,
                'type': type,
                'question_count': question_list.count,
                'planguage_list': planguage_list,
                'selected_planguage_id': planguage_id }
    
    return render(request, 'html/Question/list.html', context) # 나중에 홈 html로 바꿀 예정

# 댓글 계층 구조로 만들기
def get_comment_tree(comments):
    comment_dict = {}
    comment_id_list = []
    for comment in comments:
        if comment.parent_comment_id is None: #그냥 댓글
            comment_dict[comment.id] = {'c': comment, 'rcs': []} # c: 댓글 / rcs: 대댓글 / rr_data : 대댓글에 달린 대댓글 데이터(딕셔너리)
            comment_id_list.append(comment.id)
        else: #대댓글
            if comment.parent_comment_id in comment_dict: #그냥 댓글에 바로 달린 대댓글
                comment_dict[comment.parent_comment_id]['rcs'].append(comment)
            else: #대댓글에 달린 대댓글
                comment_dict[comment.parent_comment_id] = {'c': None, 'rcs': [comment]}
    return comment_dict, comment_id_list

#질문 상세
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    comments = Comment.objects.filter(question=question).order_by('create_date')
    comment_tree, comment_id_list = get_comment_tree(comments)
    context = {'question': question, 'comment_tree': comment_tree, 'comment_id_list': comment_id_list, 'user': request.user}
    
    # 중복 방지를 위해 쿠키 설정
    session_cookie = request.COOKIES.get('sessionid') # 로그인할 때 생기는 sessionid 쿠키 받아오기
    print(session_cookie)
    cookie_name = F'question_views:{session_cookie}' # 쿠키 이름 설정, f-string 문자열 포맷팅 이용 
    response = render(request, 'html/Question/view.html', context)

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

    return render(request, 'html/Question/view.html', context)
