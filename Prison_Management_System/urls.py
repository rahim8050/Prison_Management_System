"""
URL configuration for Prison_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from prison import views

urlpatterns = [
    path('',views.Master,name='Master'),
# path('add/warden',views.AddWarden,name='AddWarden'),
    path('Add/Warden',views.AddWarden,name='AddWarden'),
    # path('see/warden',views.Wardens,name='Wardens'),
    path('warden/view',views.Wardens,name='Wardens'),
path('Wardens/delete/<int:warden_id>', views.DeleteWarden, name='DeleteWarden'),
path('Wardens/update/<int:warden_id>', views.UpdateWarden, name='UpdateWarden'),
    path('admin/', admin.site.urls),

]
