"""GSAproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from GSAapp import views, api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', api_views.login_api),
    path('api/register/', api_views.register_api),
    path('api/add_task/', api_views.add_task_api),
    path('api/view_all_tasks/', api_views.view_all_tasks_api),
]
