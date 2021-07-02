from rest_framework import serializers

from . import models

class CreateNewRoomCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = models.RoomCategories
        fiels = ['name', 'price', 'notes']
        #extra_kwargs = {'name': {'write_only': True}}

    # def create(self, validated_data):
    #     room_category = models.RoomCategories(
    #         id=validated_data['id'],
    #         name=validated_data['name'],
    #         price=validated_data['price'],
    #         notes=validated_data['notes']
    #     )
    #     #name = set_name(validated_data['name'])
    #     room_category.save()
    #     return room_category


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rooms
        fields = ['id', 'name', 'price', 'notes']
