from django.shortcuts import render
from django.utils import timezone
from .models import Conf


def conf_list(request):
    confs = Conf.objects.filter(published_post_date__lte=timezone.now()).order_by('published_post_date')
    return render(request, 'pages/home.html', {'confs': confs})
