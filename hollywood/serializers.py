from rest_framework import serializers
from .models import HollywoodMovie

# class HollywoodMovieSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     actor = serializers.CharField(max_length=50)
#     actress = serializers.CharField(max_length=50)
#     release_date = serializers.DateField()
#     created_on = serializers.DateTimeField(required=False)

#     def create(self, validated_data):
#         return HollywoodMovie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.actor = validated_data.get('actor',instance.actor)
#         instance.actress = validated_data.get('actress',instance.actress)
#         instance.release_date = validated_data.get('release_date',instance.release_date)
#         instance.save()
#         return instance



# ModelSerializer is used over above code it also contains create and update methods which are automatically created unlike above.
class HollywoodMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = HollywoodMovie
        fields = "__all__"  

    