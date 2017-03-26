from django.shortcuts import render
from pads.models import Pad


def pad_list(request):
    pad_list = Pad.objects.all()
    template_name='pads/pad_list.html'
    return render(request, template_name, {'pad_list': pad_list})
