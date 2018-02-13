from rest_framework import serializers
from restapi.models import Problem, Rating, Solution

'''
class ProblemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_blank=True, required=False)
    author = serializers.CharField(max_length=100, allow_blank=True, required=False)
    description = serializers.CharField(max_length=100, allow_blank=True, required=False)
    difficulty = serializers.IntegerField()
    good = serializers.IntegerField()

    def create(self, validated_data):
        return Problem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.difficulty = validated_data.get('difficulty', instance.difficulty)
        instance.good = validated_data.get('good', instance.good)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
'''


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id', 'name', 'author', 'description', 'difficulty', 'good')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'title', 'date', 'rating', 'content')


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('created', 'code', 'language', 'output', 'pending')
