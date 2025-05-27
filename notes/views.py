from rest_framework import viewsets
from .serializer import NoteSerializer
from .models import Note

# Create your views here.
class NoteListView(viewsets.ModelViewSet):
     """
    ViewSet for listing, creating, updating, and deleting Note objects.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all() # type: ignore[attr-defined]