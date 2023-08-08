from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
         # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
         
        self.user = self.request.user

        if self.user.is_authenticated:
            context["user_schedule"] = self.user.schedule.all()
            
        return context