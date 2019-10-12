from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib import auth
from .models import Author

from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'myapp/main.html')

def signup(request):
    if request.method == "POST": #회원가입버튼 클릭 시
        username = request.POST.get('username')
        password = request.POST.get('password')
        psudo_password = request.POST.get('psudo_password')
        if password == psudo_password :
            user = User.objects.create_user(username=username, password=password) #장고의 createsuperuser 을 가져옴. admin 페이지에서 User테이블 확인
            author = Author()
            author.user = user
            author.email = request.POST.get('email')
            author.phone_number = request.POST.get('phone_number')
            author.save() #저장꼭!
        else : #TODO 비밀번호가 틀릴 시
            pass
        return redirect('main') #render()가 아님!!
    else:   #TODO 회원가입 페이지로 접속할때
        pass
    return render(request, 'myapp/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password) #로그인 정보 확인
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:   #TODO 로그인 정보가 없을때
            pass
        return redirect('signin')
    else:   #TODO 회원가입 페이지로 접속할때
        pass
    return render(request,'myapp/signin.html')

def logout(request):
    auth.logout(request)
    return render(request, 'myapp/logout.html')

def change_pw(request):
    if request.method =="POST":
        old_password = request.POST.get('old_password')
        user = request.user
        if check_password(old_password, user.password):
            pw1 = request.POST.get('new_password')
            pw2 = request.POST.get('new_password_chk')
            if pw1 == pw2:
                user.set_password(pw1)  #비밀번호 재지정
                user.save() #저장꼭!
                auth.login(request, user) #다시 로그인해주기
                return redirect('main')
            else:
                return HttpResponse("비밀번호가 다릅니다.")
        else:
            return HttpResponse("기존 비밀번호를 확인해 주세요")
    else:
        return render(request, 'myapp/change_pw.html')
