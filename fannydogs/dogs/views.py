from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}

]


# Create your views here.
def index(request):
    posts = FannyDogs.objects.all()


    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected':0,

    }

    return render(request, 'dogs/index.html', context=context)

def about(request):
    return render(request, 'dogs/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')


    else:
        form = AddPostForm()
    return render(request, 'dogs/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_slug):
    post = get_object_or_404(FannyDogs, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'dogs/post.html', context=context)


def show_category(request, cat_id):
    posts = FannyDogs.objects.filter(cat_id=cat_id)


    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id

    }

    return render(request, 'dogs/index.html', context=context)