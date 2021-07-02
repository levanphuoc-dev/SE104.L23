from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
#from django.http import JsonResponse
from .models import *
from django.db.models import F
from django.db.models import Q
from django.db.models import Count
from django.core.paginator import Paginator
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers

# Create your views here.

# Class View of Room CATEGORY

class AllRoomInThisCategoryView(APIView):

    def get(self, request, room_category_id):
        res = list(Rooms.objects.filter(category=room_category_id).values())
        return Response(res)

class ListAvailableRoomOfThisCategoryView(APIView):

    def get(self, request, room_category_id):
        res = list(Rooms.objects.filter(category=room_category_id, status__is_available='true').values())
        return Response(res)

class HowMuchRoomIsAvailableView(APIView):

    def get(self, request):
        res = Rooms.objects.filter(status__is_available='true').count()
        return Response(res)

class SortByCategoryView(APIView):

    def get(self, request):
        res = list(Rooms.objects.filter(status__is_available='true').order_by('category').values())
        return Response(res)

# class CreateNewRoomCategoryViewSet(viewsets.ModelViewSet):
#
#     serializer_class = serializers.CreateNewRoomCategorySerializers
#     queryset = RoomCategories.objects.all()

    # def post(self, request):
    #
    #     serializer = serializers.CreateNewRoomCategorySerializers(data=request.data)
    #
    #     if serializer.is_valid():
    #         id = serializer.data.get('id')
    #         name = serializer.data.get('name')
    #         price = serializer.data.get('price')
    #         notes = serializer.data.get('notes')
    #         return Response({'message': 'You have successfully created a new room category!'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateNewRoomCategoryView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user = JWTAuthentication().authenticate(request=request)[0]
        room_category_serializer = serializers.CreateNewRoomCategorySerializers(data=request.data)
        if room_category_serializer.is_valid():
            room_category_serializer.save()
            return Response(room_category_serializer.data, status=status.HTTP_201_CREATED)
        return Response(room_category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# CLASS VIEW OF ROOM RENT

class CheckRentView(APIView):

    def get(self, request, room_rent_ip):
        res = list(RoomRentals.objects.filter(id=room_rent_ip).values())
        return Response(res)

class AllRentalsView(APIView):

    def get(self, request):
        res = list(RoomRentals.objects.all().values())
        return Response(res)


class ReturnHead50ByDefaultView(APIView):


    #https://docs.djangoproject.com/en/3.2/topics/pagination/
    def get(self, request, filter_status_category):
        res = list(RoomRentals.objects.filter(Q(room__status=filter_status_category) | Q(room__category=filter_status_category)).order_by('start_at', 'room__status').values())
        p = Paginator(res, 50)
        page1 = p.page(1)
        return Response(page1.object_list)




# CLASS VIEW OF ROOM SERVICE

class AllServicesOfARoomView(APIView):

    def get(self, request, room_ip):
        res = list(Services.objects.filter(rental__id=room_ip).values())
        return Response(res)


# CLASS VIEW OF ROOM

class GetTop50AvailableRoomView(APIView):

    def get(self, request, filter_status_category):
        res = list(Rooms.objects.filter(Q(status=filter_status_category) | Q(category=filter_status_category)).order_by('category').values())
        p = Paginator(res, 50)
        page1 = p.page(1)
        return Response(page1.object_list)






class RoomView(APIView):
    """docstring for RoomCategoryView."""

    def get(self, request):
        info = list(Rooms.objects.values())

        return Response(info)

class AvailableRoomsView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        b = JWTAuthentication().authenticate(request=request)[0]
        c = serializers.RoomSerializer(Rooms.objects.filter(status__is_available='true'))
        c = list(c.values()) # list(Status.objects.values())

        return Response({'b': b.data, 'c': c.data})

class RoomRentalView(APIView):

    def get(self, request):
        a = list(RoomRentals.objects.filter(room__floors=2).values())

        return Response(a)


class ClientByPhoneView(APIView):

    def get(self, request, phone):
        res = list(Client.objects.filter(phone_no=phone).values())

        return Response(res)


class DontNoHowToNameView(APIView):

    def get(self, request):
        info = list(RoomRentals.objects.select_related().filter(room__status__is_available='false').values(name=F('client__full_name'), phone=F('client__phone_no'), floor=F('room__number'), Start_at=F('start_at'), checkout_at=F('check_out_at')))

        return Response(info)
