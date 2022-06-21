from rest_framework import viewsets
from sports.models import Local
from sports.serializer import LocalSerializer

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

