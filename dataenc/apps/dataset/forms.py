# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from os.path import splitext


class UploadDatasetDecForm(forms.Form):

    error_messages = {
        'invalid_format': _(u'Invalid file format. Allowed: csv.'),
        'file_size': _(u'File is very big. Maximum size: 40 MB.'),
    }

    file_dataset = forms.FileField(label=_(u'Dataset'))
    key = forms.CharField(label=_(u'key'), required=False)
    output_filename = forms.CharField(label=_(u'Output filename'),
                                      required=False)

    def clean_file_dataset(self):
        file_dataset = self.cleaned_data['file_dataset']

        # check if is csv
        filename, ext = splitext(file_dataset.name)
        if ext not in ['.csv', ]:
            raise forms.ValidationError(error_messages['invalid_format'])

        # check size
        if file_dataset.size > 41943040:
            raise forms.ValidationError(error_messages['file_size'])

        return file_dataset


class UploadDatasetEncForm(UploadDatasetDecForm):

    auto_generate_key = forms.BooleanField(label=_(u'Auto generate key'),
                                           required=False)
