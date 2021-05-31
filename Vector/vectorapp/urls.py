from django.urls import path, re_path
from vectorapp import views
from django.views.generic import TemplateView
from django_filters.views import object_filter

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
