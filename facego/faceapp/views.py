from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import Http404

# Create your views here.
from .models import *


# class UserHomeView(DetailView)


def user_posts(request, username):
    q = request.GET.get('qs')
    ex = request.GET.get('ex')
    # user = get_object_or_404(User, username=username)
    all_posts = Post.objects.filter(owner__username=username).prefetch_related('comments')
    if q:
        all_posts = all_posts.filter(content__icontains=q)
    if ex:
        all_posts = all_posts.exclude(content__icontains=ex)
    return render(request, 'faceapp/posts.html', {'posts': all_posts})


# def user_posts_search(request, username, query):
#     # user = get_object_or_404(User, username=username)
#     all_posts = Post.objects.filter(owner__username=username, content__icontains=query).prefetch_related('comments')
#     return render(request, 'faceapp/posts.html', {'posts': all_posts})


def user_home(request):
    p = request.GET.get('p')
    user = request.user
    relations = Relation.objects.filter(follower_id=user.id).values_list('followed_by_id', flat=True)
    posts = Post.objects.filter(owner_id__in=relations, deleted=False).values('id', 'content')
    if p:
        p = int(p)
        posts = posts[10 * (p - 1): 10 * p]
    return render(request, 'faceapp/user_home.html', {'posts': posts})


