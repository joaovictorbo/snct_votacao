from django.shortcuts import render
from .models import turmas
from .serializer import TurmaSerializer

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class turmaLista(ListCreateAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer

class turmadetelhes(RetrieveUpdateDestroyAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer
