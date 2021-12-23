from django.db.models import fields
from rest_framework import serializers
from .models import T20Players, ODIPlayers, TestPlayers


class T20PlayersSerializer(serializers.ModelSerializer):
    class Meta:

        model = T20Players
        fields = '__all__'


class ODIPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ODIPlayers
        fields = '__all__'


class TestPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPlayers
        fields = '__all__'
