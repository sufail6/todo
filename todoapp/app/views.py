from django.shortcuts import render, redirect


# Create your views here.
from app.forms import Card
from app.models import Mod


def home(request):
    return render(request,'home.html')


def add(request):
    data = Card()
    if request.method == 'POST':
        data = Card(request.POST)
        if data.is_valid():
            data.save()
            return redirect('view')
    return render(request,'add.html', {'data': data})


def view(request):
    data = Mod.objects.all()
    return render(request,'view.html', {'data': data})


def delete(request,id):
    data = Mod.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('view')
    else:
        return redirect('view')


def edit(request, id):
    data = Mod.objects.get(id=id)
    if request.method == 'POST':
        data = Card(request.POST or None, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            return redirect('view')
    else:
        data = Card(instance=data)
    return render(request, 'edit.html', {'data': data})
