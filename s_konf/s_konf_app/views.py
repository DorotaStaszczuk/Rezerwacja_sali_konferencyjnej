from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from s_konf_app.models import Room

# Create your views here.


class MainSiteView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'conf_template.html', ctx)


class RoomView(LoginRequiredMixin, DetailView):
    model = Room


class AddNewRoomView(View):
    model = Room
    pass


class ModifyRoomView(View):
    model = Room
    pass


class DeleteRoomView(View):
    model = Room
    pass