from django.views import View
from .models import Room
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render, redirect


# Create your views here.


class MainSiteView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'conf_template.html', ctx)


class RoomView(DetailView):
    model = Room


class AddNewRoomView(CreateView):
    model = Room
    fields = '__all__'

    def get_success_url(self):
        return reverse('room', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class ModifyRoomView(View):
    model = Room
    pass


class DeleteRoomView(View):
    model = Room
    pass