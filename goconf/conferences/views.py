from django.shortcuts import render
from django.utils import timezone
from .models import Conference


def conf_list(request):
    confs = Conference.objects.order_by('date')
    return render(request, 'pages/home.html', {'confs': confs})
