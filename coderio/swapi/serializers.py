from rest_framework import serializers 
from swapi.models import Swapi

class SwapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swapi
        fields = (
            'rating',
            'idcharacter'
        )

    def validate(self, data):
        if data['rating'] < 1 or data['rating'] > 5:
            raise serializers.ValidationError("Ratings range is 1 at 5, try again")
        return data

    def create(self, validated_data):
        return Swapi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.idcharacter = validated_data.get('idcharacter', instance.idcharacter)
        instance.save()
        return instance
