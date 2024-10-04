from rest_framework import serializers
from .models import Team, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email", "team"]


class TeamSerializer(serializers.ModelSerializer):
    people = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Person.objects.all()
    )
    class Meta:
        model = Team
        fields = ["name", "people"]
