from django.shortcuts import render

# Create your views here.
def wardens(request):

    return render(request, 'wardens.html')