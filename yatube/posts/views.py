from .models import Post, Group

from django.shortcuts import render, get_object_or_404


def index(request):
    template = 'posts/index.html'
    title = "Последние обновления на сайте"
    posts = Post.objects.all()[:10]
    context = {
        "posts": posts,
        "title": title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = "Записи сообщества"
    context = {
        'group': group,
        'posts': posts,
        "title": title,
    }
    return render(request, template, context)
