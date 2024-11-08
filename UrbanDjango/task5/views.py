from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
#from django import forms


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    login = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            print(login, password, repeat_password, age)
            if password == repeat_password and int(age) >= 18 and login not in users:
                users.append(login)
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
                elif login in users:
                    info['error'] = 'Пользователь уже существует'
    context = {'error': info, 'welcome': f'Приветствуем, {login}', 'login': login,
               'error_message': info.get('error')}
    return render(request, 'registration_page.html', context)


def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    login = None
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        print(login, password, repeat_password, age)
        if password == repeat_password and int(age) >= 18 and login not in users:
            users.append(login)
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif login in users:
                info['error'] = 'Пользователь уже существует'
    context = {'error': info, 'welcome': f'Приветствуем, {login}', 'login': login, 'error_message': info.get('error')}

    return render(request, 'registration_page.html', context)


