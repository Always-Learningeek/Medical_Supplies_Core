from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request, pid):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    post.counted_views += 1
    post.save()
    previous_post = posts.filter(id__lt=post.pk).order_by('-pk').first()
    next_post = posts.filter(id__gt=post.pk).order_by('pk').first()
    context = {'post': post, 'previous_post': previous_post, 'next_post': next_post}
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if request.method == 'GET':
        if q := request.GET.get('q'):
            posts = Post.objects.filter(content__contains=q)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
def test(request):
    posts =Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/test-blog.html', context)
