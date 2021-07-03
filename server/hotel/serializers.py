from rest_framework import serializers

from . import models


class CreateNewRoomCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = models.RoomCategories
        fields = ['name', 'price', 'notes']

class CreateRoomRentalsSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.RoomRentals
        fields = ['room', 'client', 'staff_create', 'create_at', 'start_at', 'check_out_at', 'summary']


class CreateAServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Services
        fields = ['type', 'rental', 'create_at', 'is_canceled', 'quantity', 'sub_total', 'detail']


class CreateClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = ['full_name', 'identify_card_no', 'award_point', 'phone_no', 'email_address', 'post_number', 'notes']
        


# class RoomSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Rooms
#         fields = ['category', 'status', 'floors', 'number']
