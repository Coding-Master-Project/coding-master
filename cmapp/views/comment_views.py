from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from cmapp.forms import CommentForm
from cmapp.models import Question, Answer, Comment

#답변 등록
@login_required(login_url='common:login')
def comment_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #임시 저장
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('{}#answer_{}'.format(resolve_url('cmapp:detail', question_id=question.id), comment.id))
    else:
        form = CommentForm()
    
    context = {'question': question, 'form': form}
    return render(request, 'cmapp/question_detail.html', context)