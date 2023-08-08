from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .forms import ScheduleForm
from .models import Schedule
from django.http import HttpResponseRedirect
from datetime import datetime
from django.urls import reverse_lazy

# Create your views here.
class CreateSchedule(CreateView):
    form_class = ScheduleForm
    template_name = 'schedules/schedule_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.time_created = datetime.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class DetailSchedule(DetailView):
    model = Schedule
    template_name = "schedules/schedule_detail.html"
    context_object_name = 'schedule'

class EditSchedule(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = "schedules/schedule_edit.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.time_edited = datetime.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class DeleteSchedule(DeleteView):
    model = Schedule
    template_name = "schedules/schedule_delete.html"
    context_object_name = 'schedule'
    success_url = reverse_lazy('home')