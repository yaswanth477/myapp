from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, template_name="index.html")


class HomeView(TemplateView):
    template_name = 'myfile.html'

# def myimage(request):
#     return render(request, template_name="myfile.html")