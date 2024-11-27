from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import EmptyPage, Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from  django.http import HttpResponse

from prison.apps_forms import WardenForm, ArmouryForm, LoginForm
from prison.models import Warden, Armoury


# Create your views here.



@login_required
@permission_required("prison.add_warden",raise_exception=True)
def AddWarden(request):
        if request.method == 'POST':
            form = WardenForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your warden has been added.')
                return redirect('Wardens')
        else:
            form = WardenForm()
        return render(request, 'WardenForm.html', {"form": form})
@login_required
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
@login_required
@permission_required("prison.delete_warden", raise_exception=True)
def  DeleteWarden(request, warden_id):
        warden = Warden.objects.get(id=warden_id)  # select * from Warden table  where id=??
        warden.delete()  # delete from Warden where id = ??
        messages.info(request, f"Warden {warden.FirstName} was deleted")
        return redirect('Wardens')
@login_required
@permission_required("prison.change_warden",raise_exception=True)
def UpdateWarden(request, warden_id):
    warden = get_object_or_404(Warden, id=warden_id)
    if request.method == 'POST':
        form = WardenForm(request.POST,request.FILES, instance=warden)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your warden has been updated.')
            return redirect('Wardens')
    else:
        form = WardenForm(instance=warden)
    return render(request, 'WardenUpdateForm.html', {"form": form})
@login_required
@permission_required("prison.view_warden",raise_exception=True)
def WardenDetails(request, warden_id):
    warden = Warden.objects.get(id=warden_id)
    armoury = Armoury.objects.filter(Warden=warden_id)
    return render(request, "WardenDetails.html", {"armoury": armoury, "warden": warden})

@login_required
@permission_required("prison.view_warden",raise_exception=True)
def SearchWarden(request):
    data = Warden.objects.all().order_by('id').values()
    search_term = request.GET.get('Search')
    data = Warden.objects.filter(Q(FirstName__icontains=search_term) | Q(LastName__icontains=search_term) | Q(Email__icontains=search_term) )
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page)
    except EmptyPage | pageNotAnInterger:
        paginated_data = paginator.page(1)
    return render(request,'Wardens.html',{"data": paginated_data})

# def Armoury(request,warden_id):
#     warden = get_object_or_404(Warden, id=warden_id)
#     if request.method == "POST":
#         form = ArmouryForm(request.POST)
#         if form.is_valid():
#             GunModel = form.cleaned_data['GunModel']
#             Armo = Armoury(GunModel=GunModel, status=True, warden=warden)
#             Armo.save()
#             # messages.success(request, 'Your deposit has been successfully saved')
#             return redirect('Wardens')
#     else:
#         form = ArmouryForm()
#     return render(request, 'ArmouryForm.html', {"form": form, "warden": warden})

def login_user(request):
    if request.method == 'GET':
       form = LoginForm()
       return render(request, 'LogInForm.html', {"form": form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user:
                login(request, user)
                return redirect('Wardens')
        messages.error(request, 'Invalid username or password.')
        return render(request, 'LogInForm.html', {"form": form})





@login_required
def signout_user(request):
    logout(request)
    return redirect('login')