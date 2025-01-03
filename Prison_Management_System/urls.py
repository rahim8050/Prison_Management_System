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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Prison_Management_System import settings
from prison import views

urlpatterns = [
path('warden/details/<int:warden_id>', views.WardenDetails, name='WardenDetails'),
# path('add/warden',views.AddWarden,name='AddWarden'),
    path('Add/Warden',views.AddWarden,name='AddWarden'),
    # path('see/warden',views.Wardens,name='Wardens'),
    path('',views.Wardens,name='Wardens'),
path('Wardens/delete/<int:warden_id>', views.DeleteWarden, name='DeleteWarden'),
path('Wardens/Armoury/<int:warden_id>', views.Armoury, name='Armoury'),
path('Wardens/update/<int:warden_id>', views.UpdateWarden, name='UpdateWarden'),
path('Warden/search',views.SearchWarden,name='SearchWarden'),
path('login/',views.login_user,name='login'),
path('logout/',views.signout_user,name='logout'),
    path('about',views.about,name='about'),
    path('contact',views.contact, name='contact'),
                  path('signup', views.signup, name='signup'),
    path('armoury/armoury/<int:Gun_id>', views.Armos, name='Armoury'),

    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
