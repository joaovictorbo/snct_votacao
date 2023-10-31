from django.shortcuts import render
from .models import turmas,escola
from .serializer import TurmaSerializer,VotacaoSerializer,EscolaSerializer

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView,UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination


class PaginateionTrumas(PageNumberPagination):
    page_size =10
    page_query_param = 'page_size'
    max_page_size = 100

class turmaLista(ListAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer
    pagination_class = PaginateionTrumas

    def get_queryset(self):
        return super().get_queryset()
    

class turmaCriar(CreateAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAdminUser]
    


class turmadetelhes(RetrieveUpdateDestroyAPIView):
    queryset = turmas.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAdminUser]



class Votacao(UpdateAPIView):
    queryset = turmas.objects.all()
    serializer_class = VotacaoSerializer

    def partial_update(self, request, *args, **kwargs):
        id = kwargs['pk']
        turma = turmas.objects.get(id=id)

        turma.votos += 1

        turma.save()

        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)



class escolaLista(ListAPIView):
    queryset = escola.objects.all()
    serializer_class = EscolaSerializer
    pagination_class = PaginateionTrumas

    def get_queryset(self):
        return super().get_queryset()