# -*- coding: utf-8 -*-

from ..forms import UploadDatasetEncForm
from ..forms import UploadDatasetDecForm
from ..utils import encrypt_dataset
from ..utils import decrypt_dataset
from ..utils import response_dataset
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

__all__ = ['start', 'send_dataset_enc', 'send_dataset_dec', ]


class StartView(TemplateView):

    template_name = 'dataset/start.html'

    def get_context_data(self, **kwargs):
        context = super(StartView, self).get_context_data(**kwargs)
        return context


class SendDatasetEncFormView(FormView):

    form_class = UploadDatasetEncForm
    success_url = 'dt:start'
    template_name = 'dataset/form_enc.html'

    def form_valid(self, form):
        file_sent = form.cleaned_data.get('file_dataset', None)
        output_name = form.cleaned_data.get('output_filename', None) \
            or 'output.csv'
        key = form.cleaned_data.get('key', None) or '123456'
        dataset = encrypt_dataset(file_sent, key, all_cols=True)
        return response_dataset(dataset, output_name=output_name)


class SendDatasetDecFormView(FormView):

    form_class = UploadDatasetDecForm
    success_url = 'dt:start'
    template_name = 'dataset/form_dec.html'

    def form_valid(self, form):
        file_sent = form.cleaned_data.get('file_dataset', None)
        output_name = form.cleaned_data.get('output_filename', None) \
            or 'output.csv'
        key = form.cleaned_data.get('key', None)
        dataset = decrypt_dataset(file_sent, key, all_cols=True)
        return response_dataset(dataset, output_name=output_name)


start = StartView.as_view()
send_dataset_enc = SendDatasetEncFormView.as_view()
send_dataset_dec = SendDatasetDecFormView.as_view()
