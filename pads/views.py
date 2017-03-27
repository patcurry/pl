from django.shortcuts import render
from pads.models import Pad
from pads.models import Locker


def index(request):
    pad_list = Pad.objects.all()
    locker_list = Locker.objects.all()
    pads_available = len(pad_list)
    lockers_available = len(pad_list)
    template_name='index.html'
    return render(request, template_name,
        {'pads_available': pads_available, 'lockers_available': lockers_available})


def pad_list(request):
    pad_list = Pad.objects.all()
    template_name='pads/pad_list.html'
    return render(request, template_name, {'pad_list': pad_list})


def locker_list(request):
    locker_list = Locker.objects.all()
    template_name='pads/locker_list.html'
    return render(request, template_name, {'locker_list': locker_list})
