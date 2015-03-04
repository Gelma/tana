from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^update/(?P<booking_id>\d+)$', 'bookings.views.update', name='update'),
    url(r'^delete/(?P<booking_id>\d+)$', 'bookings.views.delete', name='delete'),
)
