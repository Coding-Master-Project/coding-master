from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from cmapp.models import Question

#질문 목록(메인)
def index(request):
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

    # session_cookie = request.session['user_id']
    # cookie_name = F'question_views:{session_cookie}'
    # response = render(request, 'notice/notice_detail.html', context)

    # if request.COOKIES.get(cookie_name) is not None:
    #     cookies = request.COOKIES.get(cookie_name)
    #     cookies_list = cookies.split('|')
    #     if str(pk) not in cookies_list:
    #         response.set_cookie(cookie_name, cookies + f'|{pk}', expires=None)
    #         notice.hits += 1
    #         notice.save()
    #         return response
    # else:
    #     response.set_cookie(cookie_name, pk, expires=None)
    #     notice.hits += 1
    #     notice.save()
    #     return response


    return render(request, 'cmapp/question_detail.html', context)