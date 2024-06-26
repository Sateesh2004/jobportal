"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from core import views
from enroll import views as eviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', eviews.sign_up),
    path('sign-in/', eviews.sign_in),
    path('home/', views.home),
    path('about/', views.about),
    path('profile/', views.profile),
    path('edit-profile/', views.editprofile),
    path('jobpost/', include("jobpost.urls")),
    path('jobshow/', include("joblist.urls")),
    path('marketjobshow/', include("marketing.urls")),
    path('categoryjobshow/', include("categoryjob.urls")),
    path('applyforjob/', include("apply.urls")),
    path('log-out/', eviews.log_out),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
