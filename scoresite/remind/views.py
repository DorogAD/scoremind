from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Game, Episode

def index(request):
    return render(request, 'remind/index.html')

class Home(ListView):
    model = Game
    template_name = 'remind/index.html'
    context_object_name = 'games'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_title'] = 'Game Title'
        return context
