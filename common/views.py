from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    username_value = request.GET.get('name', '')
    valid = 0 #사용자 이름 중복 검사 결과 -> 0: 기본 / 1: 중복 / 2: 중복 x
    email_valid = 0 #이메일 중복 검사 결과
    pw_valid = "0" #비밀번호 유효성 검사 결과

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('pw_valid'))
            valid = 2
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                email_valid = 1
            if form.cleaned_data.get('pw_valid') == "2":
                pw_valid = "2"
            
            if email_valid == 0 and pw_valid == "2":
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password) #사용자 인증
                login(request, user) #로그인
                return redirect('index')
    else:
        if username_value: #중복 확인 누른 경우
            valid = 2
            if User.objects.filter(username=username_value).exists():
                valid = 1
            print("~~~")
            print(valid)
            form = UserForm(initial={'username': username_value})
        else:
            form = UserForm()

    context = { 'form': form, 'valid': valid, 'email_valid': email_valid, 'pw_valid': pw_valid}
        
    return render(request, 'html/Login/signup.html', context)

# def username_check(request):
#     username_value = request.GET.get('name', '')
#     users = User.objects.all()
#     valid = 0
#     for user in users:
#         if username_value == user.username:
#             valid = 1
#     context = { 'valid': valid }
#     print("~~~")
#     print(valid)
#     return render(request, 'html/Login/signup.html', context)
