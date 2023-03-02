from .models import spots
from django.shortcuts import render, redirect
from .forms import spot_edit


# Create your views here.
def Home(request):
    disp = spots.objects.all()
    dicto = {
        'spots': disp
    }
    return render(request, 'Home.html', dicto)


def add_spot(request):
    if request.method == 'POST':
        name = request.POST.get('spot_name')
        known = request.POST.get('spot_known')
        desc = request.POST.get('spot_desc')
        thb = request.FILES['spot_img']
        mov = spots(name=name, known=known, desc=desc, thb=thb)
        mov.save()
    return render(request, 'add.html')


def details(request, id):
    det = spots.objects.get(id=id)

    return render(request, 'details.html', {'fr': det})


def edit(request, id):
    ed = spots.objects.get(id=id)
    form = spot_edit(request.POST or None, request.FILES, instance=ed)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'edited': ed})


def dele(request, id):
    if request.method == 'POST':
        dels = spots.objects.get(id=id)
        dels.delete()
        return redirect('/')
    return render(request, 'delete.html')
