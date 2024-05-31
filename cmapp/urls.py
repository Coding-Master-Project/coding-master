from django.urls import path

from .views import profile_views, question_list_views,info_list_views,info_views, question_views, answer_views, comment_views

app_name = 'cmapp'

urlpatterns = [
    #base_views.py

    #question_list_views.py
    path('question/language/<int:planguage_id>', question_list_views.list, name='question_list'), #질문 목록(메인)
    path('question/<int:question_id>/', question_list_views.detail, name='question_detail'), #질문 상세

    #info_list_views.py
    path('info/language/<int:planguage_id>', info_list_views.list, name='info_list'),
    path('info/<int:information_id>/',info_list_views.detail, name='info_detail'),

    #question_views.py
    path('question/create/', question_views.question_create, name='question_create'), #질문 등록
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'), #질문 수정
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'), #질문 삭제
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'), #질문 추천

    #info_views,py
    path('info/create/', info_views.information_create, name='information_create'), #정보 등록
    path('info/modify/<int:information_id>/', info_views.information_modify, name='information_modify'), #정보 수정
    path('info/delete/<int:information_id>/', info_views.information_delete, name='information_delete'), #정보 삭제
    path('info/vote/<int:information_id>/', info_views.information_vote, name='information_vote'), #정보 추천

    #answer_views.py
    path('answer/create/question/<int:question_id>/', answer_views.answer_create, name='answer_create1'), #답변 등록
    path('answer/create/info/<int:information_id>/', answer_views.answer_create, name='answer_create2'), #답변 등록
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'), #답변 수정
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'), #답변 삭제
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'), #답변 추천

    #comment_views.py
    path('comment/create/question/<int:question_id>/<int:answer_id>/<int:comment_id>', comment_views.comment_create, name='comment_create1'), #댓글 등록
    path('comment/create/info/<int:information_id>/<int:comment_id>', comment_views.comment_create, name='comment_create2'),

    #profile_views.py
    path('profile/', profile_views.profile, name='profile'), #댓글 등록
]