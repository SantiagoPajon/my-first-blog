from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post

def post_list(request):
    latest_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'latest_posts': latest_posts})

def post_detail(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'blog/post_detail.html', {'post': post})
