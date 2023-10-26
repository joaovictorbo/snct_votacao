
from rest_framework import serializers
from .models import turmas



class TurmaSerializer(serializers.ModelSerializer):


    class Meta:
        model = turmas
        fields = (
            'id',
            'imagem' , 
            'titulo' ,
            'descricaoshort' ,
            'descricao' ,
            'escola' ,
            'tutor' ,
            'integrantes' 
                  )

class VotacaoSerializer(serializers.ModelSerializer):


    class Meta:
        model = turmas
        fields = (
            'votos'
                  )