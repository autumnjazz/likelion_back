from django.shortcuts import render, redirect
from .models import Post
from .models import Comment #안불러오면 NameError

def main(request):
    post_list = Post.objects.all()
    return render(request, 'main.html', {'post_list':post_list})

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "detail.html", {'post':post})
    #post 변수를 스트링 형식으로 detail.html에서 사용할수 있도록. 

def create(request):
    if request.method == "POST": #기본값 GET
        post = Post()
        post.title = request.POST.get('title')
        post.contents = request.POST.get('contents')
        post.save()
        return redirect('main')
    else:
        return render(request, 'create.html')

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete() # delete는 save를 내장하고 있다.
    return redirect("main")

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.contents = request.POST['contents']
        post.save()
        return redirect('main')
    
    else:
        return render(request, 'edit.html', {'post': post})

def comment_create(request,post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        comment = Comment(post = post) #앞의 post는 Comment()의 변수
        comment.content = request.POST['content']
        comment.save()

        return redirect('detail', post_id)
    else:
        pass