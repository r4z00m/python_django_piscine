from django.http import HttpResponse
from django.views.generic import View, ListView
import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from .forms import RemoveForm

from .models import Movies


def populate(request):
    movies = [
        {
            'episode_nb': 1,
            'title': 'The Phatom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19',
        }, {
            'episode_nb': 2,
            'title': 'Attack of th Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16',
        }, {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19',
        }, {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25',
        }, {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1980-05-17',
        }, {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25',
        }, {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J.J. Abrams',
            'producer': 'Kathleen Kennedy, J.J. Abrams, Bryan Burk',
            'release_date': '2015-12-11',
        },
    ]
    count = 0
    for elem in movies:
        try:
            if not Movies.objects.filter(episode_nb=elem['episode_nb']).count():
                Movies.objects.create(episode_nb=elem['episode_nb'], title=elem['title'], director=elem['director'],
                                      producer=elem['producer'], release_date=elem['release_date'])
                count += 1
        except Exception as error:
            return HttpResponse(error)
    if count == 0:
        return HttpResponse("Nothing to add")
    return HttpResponse("Ok " * count)


class DisplayView(ListView):
    template_name = 'ex05/display.html'
    context_object_name = 'data'
    queryset = Movies.objects.all()


class RemoveView(ListView):
    template_name = 'ex05/remove.html'

    def get(self, request, *args, **kwargs):
        try:
            data = Movies.objects.all()
            if len(data) == 0:
                return HttpResponse("No data available")
            choices = ((line.title, line.title) for line in data)
            return render(request, 'ex05/remove.html', context={'form': RemoveForm(choices)})
        except Exception as e:
            return HttpResponse("No data available")

    def post(self, request):
        try:
            data = Movies.objects.all()
            if len(data) == 0:
                return redirect('remove')
        except Exception as e:
            return redirect('remove')
        Movies.objects.filter(title=request.POST['title']).delete()
        return redirect('remove')
