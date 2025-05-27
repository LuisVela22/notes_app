from django.urls import include, path
from rest_framework import routers
from notes import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteListView, basename='notes')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
