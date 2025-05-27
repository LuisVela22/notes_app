from rest_framework import viewsets
from .serializer import NoteSerializer
from .models import Note

# Create your views here.
class NoteListView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer