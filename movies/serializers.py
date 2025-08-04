from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreModelSerializer
from actors.serializers import ActorModelSerializer


class MovieModelSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Movie
        fields = '__all__'

        
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value
    

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não pode ser maior que 200 caracteres.')
        return value
    

class MovieListDatailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreModelSerializer()
    actors = ActorModelSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']
    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None


class MovieStatsSearializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
