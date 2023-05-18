from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


##### Model Serilaizer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # Calculating custom field adding inside serializer
    len_title = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"
        # OR
        # fields = ["id", "name", "description"]
        # OR
        # exclude = ["active"]

    # Can reate extra field from given input data which will not be now saved in db but response will have this added attribute
    def get_len_title(self, object):
        length = len(object.title)
        return length

    # Field level validation
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title is too short!")
        else:
            return value

    # Object level validation
    def validate(self, data):
        if data["title"] == data["storyline"]:
            raise serializers.ValidationError("Title and storyline cannot be same")
        else:
            return data


class StreamPlatformSerializer(serializers.ModelSerializer):
    # All related data from watchlist with foreign key relation
    watchlist = WatchListSerializer(many=True, read_only=True)

    # Only selectede data from foreign table returned by __str__ of model class
    # watchlist = serializers.StringRelatedField(many=True)

    # Rather than string just select primary key to show
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # Select foreign relation data as hyperlink field linke for that object like "http://localhost:8000/watch/2"
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="watchlist-detail"
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"


##### Regular Serializer
# # Validators
# def name_length(value):
#     if len(value) > 50:
#         raise serializers.ValidationError("Name is too long!")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)

#     # Add validator if any
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name")
#         instance.description = validated_data.get("description")
#         instance.active = validated_data.get("active")
#         instance.save()
#         return instance

#     # Field level validation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value

#     # Object level validation
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title and description cannot be same")
#         else:
#             return data
