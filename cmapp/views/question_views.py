from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from cmapp.forms import QuestionForm
from cmapp.models import Question, PLanguage

#질문 등록
@login_required(login_url='common:login')
def question_create(request):
    planguage_list = PLanguage.objects.all()

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES) # 파일(이미지) 정보는 request.FILES 방식으로 받기 때문에 추가
        if form.is_valid():
            question = form.save(commit=False) #임시 저장
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('cmapp:question_list', 0)
    else:
        form = QuestionForm()
    
    context = {'form': form, 'planguage_list': planguage_list}
    return render(request, 'html/Question/write.html', context)

#질문 수정
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    planguage_list = PLanguage.objects.all()
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('cmapp:question_detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('cmapp:question_detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
        selected_planguage_id = question.planguage.id
    context = {'form': form, 'planguage_list': planguage_list, 'selected_planguage_id': selected_planguage_id}
    return render(request, 'html/Question/write.html', context)

#질문 삭제
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('cmapp:question_detail', question_id=question.id)
    question.delete()
    return redirect('cmapp:question_list', 0)

#질문 추천
@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user in question.voter.all():
        question.voter.remove(request.user)
    else:
        if request.user in question.voter.all():
            question.voter.remove(request.user)
        else:
            question.voter.add(request.user)
    return redirect('cmapp:question_detail', question_id=question.id)
