from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Club
from players.models import Player  

class ClubListView(ListView):
    model = Club
    template_name = 'clubs/club_list.html'
    context_object_name = 'clubs'
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        queryset = Club.objects.all()
        country = self.request.GET.get('country')
        league = self.request.GET.get('league')

        if country and country != 'All':
            queryset = queryset.filter(country=country)

        if league:
            queryset = queryset.filter(league__icontains=league)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Club.objects.values('country').distinct()
        context['leagues'] = Club.objects.values('league').distinct()
        return context


class ClubDetailView(DetailView):
    model = Club
    template_name = 'clubs/club_detail.html'
    context_object_name = 'club'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.filter(current_club=self.object)
        return context

class ClubCreateView(CreateView):
    model = Club
    template_name = 'clubs/club_form.html'
    fields = ['name', 'value', 'country', 'emblem', 'league']
    success_url = reverse_lazy('club-list')


class ClubUpdateView(UpdateView):
    model = Club
    template_name = 'clubs/club_form.html'
    fields = ['name', 'value', 'country', 'emblem', 'league']
    success_url = reverse_lazy('club-list')


class ClubDeleteView(DeleteView):
    model = Club
    template_name = 'clubs/club_confirm_delete.html'
    success_url = reverse_lazy('club-list')
