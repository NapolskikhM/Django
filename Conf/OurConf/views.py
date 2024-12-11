"""
модуль views фреймворка Django
вывод постов конференции

Functions:
post_list(request) -> func

"""

from django.shortcuts import render
from django.core.paginator import Paginator
from OurConf.models import Post
from OurConf.forms import Posts_on_PageForm


posts_on_pages = 5

def post_list(request):
    """вывод постов"""

    global posts_on_pages

    # выбор числа постов на одной странице
    if request.POST:
        form = Posts_on_PageForm(request.POST)
        if form.is_valid():
            posts_on_pages = form.cleaned_data["posts_on_pages"]

    # получаем все посты из базы
    posts = Post.objects.all().order_by('created_at')

    # создаем пагинатор
    paginator = Paginator(posts, posts_on_pages)

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)

    context = {'page_posts': page_posts, 'posts_on_pages': posts_on_pages}

    # передаем контекст в шаблон
    return render(request, 'index.html', context)


