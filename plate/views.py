from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

# Create your views here.
def create(request):
  if request.method=="POST":
    post = Post()
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.date = timezone.now()
    post.image = request.FILES['image']
    post.save()
    return redirect('/detail/'+str(post.id),{'post':post})
  else:
    post = Post()
    return render(request,'create.html',{'post':post})

  # 예외처리
  try:
      post.image = request.FILES['image']
  except:
      post.image = None
