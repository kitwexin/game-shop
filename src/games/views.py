from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from . import models
from django.urls import reverse_lazy


class GamesListView(ListView):
    model = models.Game
    template_name = 'games/list.html'
    paginate_by = 10


class GamesCreateView(CreateView):
    model = models.Game
    template_name = 'games/create.html'
    fields = ('__all__')

    def get_success_url(self):
        return reverse_lazy('games:list')


class GamesUpdateView(UpdateView):
    model = models.Game
    template_name = 'games/update.html'
    fields = ('__all__')

    def get_success_url(self):
        return reverse_lazy('games:detail', kwargs = {'pk' : self.object.pk})


class GamesDeleteView(DeleteView):
    model = models.Game
    template_name = 'games/delete.html'

    def get_success_url(self):
        return reverse_lazy('games:list')


class GamesDetailView(DetailView):
    model = models.Game
    template_name = 'games/detail.html'