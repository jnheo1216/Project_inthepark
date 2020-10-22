"""inthepark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from posts import views
from posts.models import Park_number

app_name = "posts"

urlpatterns = [
    path('<str:area_name>/lists/', views.p_lists, name='lists'),
    path('<int:park_num>/detail/', views.p_detail, name="detail"),
    path('makedb/', views.p_makedb, name='makedb'),
    path('write_post/<int:p_idx>', views.write_post, name='write_post'),
]
