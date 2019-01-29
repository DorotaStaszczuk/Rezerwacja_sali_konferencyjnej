"""s_konf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from s_konf_app.views import MainSiteView, RoomView, AddNewRoomView, ModifyRoomView, DeleteRoomView, ReservationView,\
    SearchView, AddNewReservationView, ModifyReservationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', MainSiteView.as_view(), name='main'),
    url(r'^room/(?P<pk>(\d)+)/$', RoomView.as_view(), name="room"),
    url(r'^room/new$', AddNewRoomView.as_view(), name="new-room"),
    url(r'^room/modify/(?P<pk>\d+)/$', ModifyRoomView.as_view(), name="modify-room"),
    url(r'^delete_room/(?P<pk>(\d)+)/$', DeleteRoomView.as_view(), name="delete-room"),
    url(r'^reservation/(?P<pk>(\d)+)/$', ReservationView.as_view(), name="reservation"),
    url(r'^reservation/new/(?P<pk>\d+)/$', AddNewReservationView.as_view(), name="new-reservation"),
    url(r'^reservation/modify/(?P<pk>(\d)+)/$', ModifyReservationView.as_view(), name="modify-reservation"),
    url(r'^search$', SearchView.as_view(), name="search"),

]
