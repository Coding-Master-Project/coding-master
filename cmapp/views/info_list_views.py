from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from cmapp.models import Comment, PLanguage, Information

#정보 목록(메인)
def list (request, planguage_id):
    print(planguage_id)
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #검색어
    type = request.GET.get('type', 'search-title') #검색 타입

    if planguage_id == 0 :
        information_list = Information.objects.order_by('-create_date')
    else :
        planguage = PLanguage.objects.filter(id=planguage_id).first()

        if planguage:
            information_list = Information.objects.filter(planguage=planguage).order_by('-create_date')

    if kw:
        if type == 'search-title': #제목 검색
            information_list = information_list.filter(
                Q(subject__icontains=kw) 
            )
        elif type == 'search-content': #내용 검색
            information_list = information_list.filter(
                Q(content__icontains=kw) 
            )
        elif type == 'search-t+c': #제목+내용 검색
            information_list = information_list.filter(
                Q(subject__icontains=kw) | #제목
                Q(content__icontains=kw) #내용
            ).distinct() #distinct는 중복 처리

    paginator = Paginator(information_list, 10) #페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    planguage_list = PLanguage.objects.all()
    context = {'information_list': page_obj,
                'page': page,
                'kw': kw,
                'type': type,
                'information_count': information_list.count,
                'planguage_list': planguage_list,
                'selected_planguage_id': planguage_id }
    
    return render(request, 'html/Information/list.html', context) # 나중에 홈 html로 바꿀 예정

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

#정보 상세
def detail(request, information_id):
    information = get_object_or_404(Information, pk=information_id)
    comments = Comment.objects.filter(information=information).order_by('create_date')
    comment_tree, comment_id_list = get_comment_tree(comments)
    context = {'information': information, 'comment_tree': comment_tree, 'comment_id_list': comment_id_list, 'user': request.user }
    
    # 중복 방지를 위해 쿠키 설정
    session_cookie = request.COOKIES.get('sessionid') # 로그인할 때 생기는 sessionid 쿠키 받아오기
    print(session_cookie)
    cookie_name = F'info_views:{session_cookie}' # 쿠키 이름 설정, f-string 문자열 포맷팅 이용 
    response = render(request, 'html/Information/view.html', context)

    if request.COOKIES.get(cookie_name) is not None: # 사용자가 글을 1개라도 조회했을 때
        cookies = request.COOKIES.get(cookie_name) # 현재 클라이언트의 쿠키 얻어오기
        cookies_list = cookies.split('|') # 파싱(question.id로 이루어진 list)
        if str(information_id) not in cookies_list: # 쿠키 리스트에 현재 question_id가 없으면 (= 조회수 중복이 아닌 경우)
            response.set_cookie(cookie_name, cookies + f'|{information_id}', expires=None) # 현재 쿠키들 뒤에 | 붙이고, question_id 쿠키 추가 (expires=None : 세션 쿠키 -> 브라우저(탭 말고 전체)를 종료할 때 쿠키 만료)
            information.views += 1 # 조회수 증가
            information.save() # 데이터베이스 변경 사항 저장
            return response
    else: # 사용자가 글을 아예 조회하지 않았을 때
        response.set_cookie(cookie_name, information_id, expires=None) # question_id 쿠키 설정
        information.views += 1 # 조회수 증가
        information.save() # 데이터베이스 변경 사항 저장
        return response

    return render(request, 'html/Information/view.html', context)
