from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from cmapp.forms import CommentForm
from cmapp.models import Question, Answer, Comment

#댓글 등록
@login_required(login_url='common:login')
def comment_create(request, question_id, answer_id, comment_id):
    print('*')
    print(comment_id)
    not_recomment_id = 0
    not_answer_id = 0
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #임시 저장
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            if (comment_id != not_recomment_id): #그냥 댓글이면
                comment.parent_comment_id = comment_id
            if (answer_id != not_answer_id): # 답변에 달린 댓글이면
                comment.answer_id = answer_id
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('cmapp:detail', question_id=question.id), comment.id))
    else:
        form = CommentForm()

    return redirect('cmapp:detail', question_id=question.id)