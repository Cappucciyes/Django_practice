from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from .forms import ScheduleForm
from .models import Schedule
from django.http import HttpResponseRedirect

# Create your views here.
class CreateSchedule(CreateView):
    form_class = ScheduleForm
    template_name = 'schedules/schedule_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class DetailSchedule(DetailView):
    model = Schedule
    template_name = "schedules/schedule_detail.html"
    context_object_name = 'schedule'