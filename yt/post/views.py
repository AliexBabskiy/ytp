from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
#from django.http import HttpResponse
from .models import Post, Group

# def index(request):

#     posts = Post.objects.order_by('-pub_date')[:10]

#     context = {
#         'posts': posts,
#     }
#     return render(request, 'post/index.html', context)

def index(request):
    """Главная страница с пагинацией."""
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'post/index.html', context)

def group_post(request, slug):
    """Страница группы с пагинацией."""
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'post/group_list.html', context)

# def profile(request, username):
#     """Страница профиля пользователя."""
#     author = get_object_or_404(get_user_model(), username=username)
#     post_list = author.posts.all().order_by('-pub_date')
#     paginator = Paginator(post_list, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     context = {
#         'author': author,
#         'page_obj': page_obj,
#     }
#     return render(request, 'post/profile.html', context)  # 'post/'
def profile(request, username):
    """Страница профиля пользователя."""
    # Получаем пользователя
    author = get_object_or_404(get_user_model(), username=username)
    
    # Получаем все посты пользователя через post_set (т.к. нет related_name в модели)
    post_list = author.post_set.all().order_by('-pub_date')  # ← изменили с posts на post_set
    
    # Добавляем пагинацию
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'author': author,
        'page_obj': page_obj,
        'post_count': post_list.count(),
    }
    
    return render(request, 'post/profile.html', context)


def post_detail(request, post_id):
    """Страница отдельного поста."""
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)  # 'post/'

# -----------------------------------------------------------------------------------------------------------------------------------------------
