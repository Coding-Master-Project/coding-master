from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from cmapp.forms import QuestionForm
from cmapp.models import Question, PLanguage
from itertools import chain

#프로필
@login_required(login_url='common:login')
def profile(request):    
    user = request.user
    
    questions =user.author_question.all()
    informations = user.author_information.all()
    post_list = list(chain(questions, informations))
    sorted_post_list = sorted(post_list, key=lambda x: x.create_date)[:3]

    for sorted_post in sorted_post_list:
        print(sorted_post.get_model_name())
    comments =user.author_comment.all()
    answers = user.author_answer.all()
    ca_list = list(chain(comments, answers))
    sorted_ca_list = sorted(ca_list, key=lambda x: x.create_date)[:2]

    voted_questions = user.voter_question.all()
    voted_informations = user.voter_information.all()
    voted_list = list(chain(voted_questions, voted_informations))
    sorted_voted_list = sorted(voted_list, key=lambda x: x.create_date)[:2]

    context = { 'sorted_post_list': sorted_post_list, 'sorted_ca_list': sorted_ca_list, 'sorted_voted_list': sorted_voted_list}
    return render(request, 'html/profile.html', context) # 나중에 홈 html로 바꿀 예정