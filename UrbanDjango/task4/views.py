from django.shortcuts import render


def main_page(request):
    return render(request, 'main_page.html')


def page_circus(request):
    circus1 = 'На Цветном'
    circus2 = 'На Конюшенной'
    circus3 = 'В Диснейленде'
    buy = 'Купить билет'
    context = {'circus': [circus1,
               circus2,
               circus3],
               'buy': buy}
    return render(request, 'circus_page.html', context)


def page_museum(request):
    museum1 = 'Третьяковка'
    museum2 = 'Русский музей'
    museum3 = 'Метрополитен'
    buy = 'Купить билет'
    context = {'museums': [museum1,
               museum2,
               museum3],
               'buy': buy}
    return render(request, 'museum_page.html', context)