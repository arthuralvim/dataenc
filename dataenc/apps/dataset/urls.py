# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    'dataset.views',
    url(r'^$', 'start', name='start'),
    url(r'^send-dataset-enc/$', 'send_dataset_enc', name='dataset_enc'),
    url(r'^send-dataset-dec/$', 'send_dataset_dec', name='dataset_dec'),
)
