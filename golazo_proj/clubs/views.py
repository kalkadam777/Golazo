from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Club
from .serializers import ClubSerializer

# logger = logging.getLogger('clubs')

class ClubListView(generics.ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'value', 'league']
    ordering = ['name']  

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        league = self.request.query_params.get('league', None)
        if country and country != 'All':
            queryset = queryset.filter(country=country)
        if league and league.strip():
            queryset = queryset.filter(league=league)

        return queryset

class ClubDetailView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubCreateView(generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer