
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

    nomeEscola = serializers.PrimaryKeyRelatedField(source='escolaID.name',read_only='True')

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
            'nomeEscola',
            'votos'
                  )

class VotacaoSerializer(serializers.ModelSerializer):


    class Meta:
        model = turmas
        fields = (
            'votos',
                  )