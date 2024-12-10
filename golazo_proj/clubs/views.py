import logging
from .models import Club
from rest_framework import generics
from .serializers import ClubSerializer
from rest_framework.exceptions import APIException

# Настраиваем логгер
logger = logging.getLogger('clubs')

class ClubListView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    ordering = ['name']

    def list(self, request, *args, **kwargs):
        try:
            logger.info("API accessed: List of clubs.")
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error retrieving club list: {e}")
            raise APIException("Failed to retrieve club list.")


class ClubDetailView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            club = self.get_object()
            logger.info(f"Club details accessed: {club.name} (ID: {club.id}).")
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error retrieving club details: {e}")
            raise APIException("Failed to retrieve club details.")


class ClubCreateView(generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def create(self, request, *args, **kwargs):
        try:
            logger.info(f"Attempting to create a new club: {request.data}")
            response = super().create(request, *args, **kwargs)
            logger.info("Club created successfully.")
            return response
        except Exception as e:
            logger.error(f"Error creating club: {e}")
            raise APIException("Failed to create club.")


class ClubUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def update(self, request, *args, **kwargs):
        try:
            club = self.get_object()
            logger.info(f"Updating club: {club.name} (ID: {club.id}) with data: {request.data}")
            response = super().update(request, *args, **kwargs)
            logger.info("Club updated successfully.")
            return response
        except Exception as e:
            logger.error(f"Error updating club: {e}")
            raise APIException("Failed to update club.")


class ClubDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            club = self.get_object()
            logger.info(f"Deleting club: {club.name} (ID: {club.id}).")
            response = super().destroy(request, *args, **kwargs)
            logger.info("Club deleted successfully.")
            return response
        except Exception as e:
            logger.error(f"Error deleting club: {e}")
            raise APIException("Failed to delete club.")
