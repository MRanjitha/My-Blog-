from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm

def post_list(request):
	posts = Post.objects.exclude(name=None).values()
	return render(request, 'blog/Sample.html',{'posts': posts})
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
