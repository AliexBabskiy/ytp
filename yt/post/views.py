from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'post': posts,
    }
    return render(request, 'post/index.html', context)

# def index(request):
#     #return HttpResponse('Главная страница')
#     template = 'post/index.html'
#     text = 'Это главная страница проекта Yatube'
#     context = {
#         'text': text,
#     }
#     return render(request, template, context)



def group_post_list(request):
    #return HttpResponse('Список мороженого')
    template = 'post/group_post_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_post_detail(request, slug):
    return HttpResponse(f'Мороженое номер {slug}')