from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from . import models
from django.urls import reverse_lazy


class GenresListView(ListView):
    model = models.Genre
    template_name = 'genres/list.html'
    paginate_by = 10


class GenresCreateView(CreateView):
    model = models.Genre
    template_name = 'genres/create.html'
    fields = ('__all__')

    def get_success_url(self):
        return reverse_lazy('genres:list')


class GenresUpdateView(UpdateView):
    model = models.Genre
    template_name = 'genres/update.html'
    fields = ('__all__')

    def get_success_url(self):
        return reverse_lazy('genres:detail', kwargs = {'pk' : self.object.pk})


class GenresDeleteView(DeleteView):
    model = models.Genre
    template_name = 'genres/delete.html'

    def get_success_url(self):
        return reverse_lazy('genres:list')


class GenresDetailView(DetailView):
    model = models.Genre
    template_name = 'genres/detail.html'