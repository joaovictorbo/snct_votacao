
from rest_framework import serializers
from .models import turmas,escola

class EscolaSerializer(serializers.ModelSerializer):

    class Meta:
        model = escola
        fields = (
            'id',
            'name' , 
                  )


class TurmaSerializer(serializers.ModelSerializer):


    class Meta:
        model = turmas
        fields = (
            'id',
            'imagem' , 
            'titulo' ,
            'descricao' ,
            'escolaID' ,
            'tutor' ,
            'integrantes',
            'votos'
                  )

class VotacaoSerializer(serializers.ModelSerializer):


    class Meta:
        model = turmas
        fields = (
            'votos',
                  )