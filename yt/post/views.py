from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    #return HttpResponse('Главная страница')
    template = 'post/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)



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