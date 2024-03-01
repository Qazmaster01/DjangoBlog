from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from aset.models import Aset, Category

menu = [{'title': "Блог", 'url_name': 'blog'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
data_db = [
    {'id': 1, 'title': 'Хочу стать крутым бэкендером', 'content': 'Бэкендер', 'is_published': True},
    {'id': 2, 'title': 'Хочу легко решать сложные задачи', 'content': 'Литкод', 'is_published': False},
    {'id': 3, 'title': 'Хочу устроиться на работу айтишником', 'content': 'Работа', 'is_published': True},
]

def index(request):
    posts = Aset.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'aset/index.html', context=data)

def blog(request):
    return render(request, 'aset/about.html', {'title': 'Блог', 'menu': menu})

def contact(request):
    return HttpResponse('<h1>Обратная связь</h1>')

def add_page(request):
    return HttpResponse('<h1>Добавить статью</h1>')

def show_post(request, post_slug):
    post = get_object_or_404(Aset, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'aset/post.html', data)

def login(request):
    return HttpResponse('<h1>Авторизация</h1>')

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Aset.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'aset/post.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
