from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def func(request):
    return render(request, 'func.html')


class class_(TemplateView):
    template_name = 'class_.html'