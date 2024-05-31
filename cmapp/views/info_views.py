from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from cmapp.forms import InfoForm
from cmapp.models import Information

#질문 등록
@login_required(login_url='common:login')
def information_create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES) # 파일(이미지) 정보는 request.FILES 방식으로 받기 때문에 추가
        if form.is_valid():
            information = form.save(commit=False) #임시 저장
            information.author = request.user
            information.create_date = timezone.now()
            information.save()
            return redirect('cmapp:info_list')
    else:
        form = InfoForm()
    
    context = {'form': form}
    return render(request, 'html/Information/write.html', context)

#질문 수정
@login_required(login_url='common:login')
def information_modify(request, information_id):
    information = get_object_or_404(Information, pk=information_id)
    if request.user != information.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('cmapp:info_detail', information_id=information.id)
    if request.method == "POST":
        form = InfoForm(request.POST, request.FILES, instance=information)
        if form.is_valid():
            information = form.save(commit=False)
            information.modify_date = timezone.now()  # 수정일시 저장
            information.save()
            return redirect('cmapp:info_detail', information_id=information.id)
    else:
        form = InfoForm(instance=information)
    context = {'form': form}
    return render(request, 'cmapp/information_form.html', context)

#질문 삭제
@login_required(login_url='common:login')
def information_delete(request, information_id):
    information = get_object_or_404(Information, pk=information_id)
    if request.user != information.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('cmapp:info_detail', information_id=information.id)
    information.delete()
    return redirect('cmapp:info_list')

#질문 추천
@login_required(login_url='common:login')
def information_vote(request, information_id):
    information = get_object_or_404(Information, pk=information_id)
    if request.user == information.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        if request.user in information.voter.all():
            information.voter.remove(request.user)
        else:
            information.voter.add(request.user)
    return redirect('cmapp:info_detail', information_id=information.id)