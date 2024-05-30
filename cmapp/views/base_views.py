from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from cmapp.models import Question, Comment, PLanguage

#홈(메인 index)
def index(request):
    return render(request, 'html/Home/home.html')