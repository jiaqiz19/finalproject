from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Avg, Max, Min, Count

from .models import Sq
from .form import SquirrelForm


def index(request):
    sqs=Sq.objects.all()
    context = {
        'sqs': sqs,
    }
    return render(request, 'sightings/index.html', context)


def edit(request, squirrel_id):
    sighting = Sq.objects.get(uid=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance=sighting)
    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)


def delete(request, squirrel_id):
    sighting = Sq.objects.filter(uid=squirrel_id)
    sighting.delete()
    return redirect(f'/sightings')


def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()
    context = {
        'form': form,
    }
    return render(request, 'sightings/add.html', context)
