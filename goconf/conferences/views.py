# from django.shortcuts import render
# from django.utils import timezone
# from .models import Conference


# def conf_list(request):
#     confs = Conference.objects.order_by('date')
#     return render(request, 'pages/home.html', {'confs': confs})

from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Conference
from django.shortcuts import get_object_or_404, render


class Conference_list(ListView):
    model = Conference


class Conference_detail(DetailView):
    model = Conference

    def conference_detail(self, request, primary_key):
        conference = get_object_or_404(Conference, pk=primary_key)
        return render(request, 'conferences/conference_detail.html', context={'conference': conference})
