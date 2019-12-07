from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Avg, Max, Min, Count

import json
from .models import Sq
from .form import SquirrelForm

def index(request):
    sqs = Sq.objects.all()
    context = {
        'sqs': sqs,
    }
    return render(request, 'sightings/index.html', context)

def stats(request):
    sqs = Sq.objects.all()
    adultCount = 0
    colorSet = set()
    runningCount = 0
    climbingCount = 0
    eatingCount = 0
    for sq in sqs:
        if sq.age == 'Adult':
            adultCount += 1
        if sq.color != None and sq.color != "":
            colorSet.add(sq.color)
        if sq.running == 'true':
            runningCount += 1
        if sq.climbing == 'true':
            climbingCount += 1
        if sq.eating == 'true':
            eatingCount += 1

    context = {
        'adultCount': adultCount,
        'colors': list(colorSet),
        'runningCount': runningCount,
        'climbingCount': climbingCount,
        'eatingCount': eatingCount,
    }
    return render(request, 'sightings/stats.html', context)

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

def showmap(request):
    sqs = Sq.objects.all()[0:100]
    sqList = [{"X": float(sq.X), "Y": float(sq.Y), "ID": sq.uid} for sq in sqs]
    context = {'sightings': json.dumps(sqList)}
    return render(request, 'sightings/map.html', context)
