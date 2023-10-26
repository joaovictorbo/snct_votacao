from django.shortcuts import render
from .models import turmas
from .serializer import TurmaSerializer,VotacaoSerializer

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView,UpdateAPIView


class turmaLista(ListAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer


    
    def get_queryset(self):
        return super().get_queryset()
    

class turmaCriar(CreateAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer
    


class turmadetelhes(RetrieveUpdateDestroyAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer


class Votacao(UpdateAPIView):
    queryset = turmas.objects.all()
    serializer_class = VotacaoSerializer