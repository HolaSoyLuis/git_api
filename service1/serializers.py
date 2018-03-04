from rest_framework import serializers
from .models import Serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')


'''
class SerieSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    release_date = serializers.DateField()
    rating = serializers.IntegerField()
    category = serializers.ChoiceField(choices=Serie.CATEGORIES_CHOICES)

# Create and return a new `Serie` instance, given the validated data.
    def create(self, validated_data):
        return Serie.objects.create(**validated_data)

# Update and return an existing `Serie` instance, given the validated
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
'''

'''
from service1.models import Serie
from service1.serializers import SerieSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime
release_date = datetime.strptime('17-04-2011', '%d-%m-%Y').date()
serie = Serie(name='Game of Thrones', category='drama', release_date=release
serie.save()
release_date = datetime.strptime('24-06-2015', '%d-%m-%Y').date()
serie = Serie(name
'''


