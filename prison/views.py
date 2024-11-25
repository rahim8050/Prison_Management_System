from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render, redirect, get_object_or_404
from  django.http import HttpResponse

from prison.apps_forms import WardenForm
from prison.models import Warden


# Create your views here.



def Master(request):
    return render (request, 'Master.html')

def AddWarden(request):
        if request.method == 'POST':
            form = WardenForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('Master')
        else:
            form = WardenForm()
        return render(request, 'WardenForm.html', {"form": form})

def Wardens(request):
    data = Warden.objects.all()
    data = Warden.objects.all().order_by('id').values()  # ORM select * from customers
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page)
    except  EmptyPage:
        paginated_data = paginator.page(1)
    return render(request, "Wardens.html", {"data": paginated_data})
def  DeleteWarden(request, warden_id):
        warden = Warden.objects.get(id=warden_id)  # select * from Warden table  where id=??
        warden.delete()  # delete from Warden where id = ??
        return redirect('Wardens')

def UpdateWarden(request, warden_id):
    warden = get_object_or_404(Warden, id=warden_id)
    if request.method == 'POST':
        form = WardenForm(request.POST, instance=warden)
        if form.is_valid():
            form.save()
            return redirect('Wardens')
