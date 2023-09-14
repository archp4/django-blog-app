from django.shortcuts import render
from blog.models import Category, Post


# Create your views here.
def home(request):
    # load 10 post
    posts = Post.objects.all()[:3]
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'home.html', data)


def post(request, url):
    # sending post
    post_data: object = Post.objects.get(postId=url)
    cat_id: object = Category.objects.get(title=post_data.catId)
    cats = Category.objects.all()
    data = {
        'catId': cat_id.catId,
        'post': post_data,
        'cats': cats,
    }
    return render(request, 'posts.html', data)


def cat(request, url):
    # # sending post
    posts = Post.objects.filter(catId=url)
    cats = Category.objects.all()
    cat = Category.objects.get(catId=url)
    data = {
        'catId': url,
        'posts': posts,
        'cats': cats,
        'selectCat': cat,
    }
    return render(request, 'categories.html', data)
