from django.urls import path

from .views import base_views, question_views, answer_views, comment_views

app_name = 'cmapp'

urlpatterns = [
    #base_views.py
    path('', base_views.index, name='index'), #질문 목록(메인)
    path('<int:question_id>/', base_views.detail, name='detail'), #질문 상세

    #question_views.py
    path('question/create/', question_views.question_create, name='question_create'), #질문 등록
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'), #질문 수정
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'), #질문 삭제
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'), #질문 추천

    #answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'), #답변 등록
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'), #답변 수정
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'), #답변 삭제
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'), #답변 추천

    #comment_views.py
    path('comment/create/<int:question_id>/<int:answer_id>/<int:comment_id>', comment_views.comment_create, name='comment_create'), #댓글 등록
]