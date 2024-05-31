from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from cmapp.forms import QuestionForm
from cmapp.models import Question, PLanguage

#프로필
@login_required(login_url='common:login')
def profile(request):    
    context = { 'user': request.user }
    return render(request, 'html/profile.html') # 나중에 홈 html로 바꿀 예정