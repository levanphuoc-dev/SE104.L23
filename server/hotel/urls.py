from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt import views as jwt_views

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    # category
    path(r'category/get-all-room-in-this-category/<room_category_id>', views.AllRoomInThisCategoryView.as_view()),
    path(r'category/list-available-room-of-this-category/<room_category_id>', views.ListAvailableRoomOfThisCategoryView.as_view()),
    url(r'^category/how-much-room-is-available/', views.HowMuchRoomIsAvailableView.as_view()),
    url(r'^category/sort-by-category/', views.SortByCategoryView.as_view()),
    url(r'^category/create-new-a-category/', views.CreateNewRoomCategoryView.as_view()),

    # rent
    path(r'rent/get-room-rent/<room_rent_ip>', views.CheckRentView.as_view()),
    url(r'^rent/get-all-rentals/', views.AllRentalsView.as_view()),
    path(r'rent/get-50-head-by-default/<filter_status_category>', views.ReturnHead50ByDefaultView.as_view()),
    url(r'^rent/create-room-rentals/', views.CreateRoomRentalsView.as_view()),

    # services
    path(r'services/get-all-services-of-a-room/<room_ip>', views.AllServicesOfARoomView.as_view()),
    url(r'^services/create-a-service/', views.CreateAServiceView.as_view()),

    # rooms
    path(r'get-top-50-available-room/<filter_status_category>', views.GetTop50AvailableRoomView.as_view()),

    # services
    path(r'checkout/all-services/<rental_id>', views.AllServicesView.as_view()),

    # client
    path(r'client/get_client_by_phone/<phone>', views.ClientInformationByPhoneView.as_view()),
    url(r'^client/create-client/', views.CreateClientView.as_view()),

    #url(r'^get_dont_know_how_to_name/', views.DontNoHowToNameView.as_view()),
]


# https://docs.djangoproject.com/en/3.2/topics/http/urls/?fbclid=IwAR3qe-Mk25FMtJxOkrCqoBZiSA0s9-MpjO6ROITgAgmcjyt2aCqJ89p7Kpo
