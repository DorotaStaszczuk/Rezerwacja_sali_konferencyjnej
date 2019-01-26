from django.views import View
from .models import Room, Reservation
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Create your views here.


class MainSiteView(View):
    def get(self, request):
        ctx = {'rooms': Room.objects.all()}
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


class ModifyRoomView(UpdateView):
    model = Room
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('room', args=[self.object.pk])


class DeleteRoomView(DeleteView):
    model = Room
    success_url = reverse_lazy("main")


class ReservationView(DetailView):
    model = Reservation


class AddNewReservationView(CreateView):
    model = Reservation
    fields = ('date', 'comment')

    def get_success_url(self):
        return reverse('reservation', kwargs={'pk': self.object.pk})


class ModifyReservationView(UpdateView):
    model = Reservation
    fields = ('date', 'comment')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('reservation', args=[self.object.pk])


class SearchView(View):
    def get(self, request):
        return render(request, 'search_form.html')
