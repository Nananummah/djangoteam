from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'postslist': posts})	
	
def detail(request, post_id):
	post = Post.objects.get(pk=post_id)
	return render(request, 'blog/detail.html', {'post': post})	
