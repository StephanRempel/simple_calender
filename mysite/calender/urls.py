from django.urls import path
from django.conf.urls import url

from . import views
app_name = 'calender'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.calendar, name='calendar'),
    url('', views.calendar, name='calendar'),
    url('add_event$', views.add_event, name='add_event'),
    url('update$', views.update, name='update'),
    url('^remove', views.remove, name='remove'),
]