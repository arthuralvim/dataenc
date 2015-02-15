# -*- coding: utf-8 -*-

from Crypto.Cipher import XOR
from django.http import HttpResponse
import base64
import csv
import functools
import pandas as pd


def func_encrypt(key, plaintext):
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plaintext))


def func_decrypt(key, ciphertext):
    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(ciphertext))


def encrypt_dataset(path_dataset, key, col=0, all_cols=False):
    dataset = pd.read_csv(path_dataset, header=None, sep=';', quotechar='"')
    encrypt = functools.partial(func_encrypt, key)

    if all_cols:
        encrypted_dataset = dataset.applymap(encrypt)

    # dataset['column'] = dataset['column'].apply(encrypt)
    # dataset.drop('column', axis=1, inplace=True)

    return encrypted_dataset


def decrypt_dataset(path_dataset, key, col=0, all_cols=False):
    dataset = pd.read_csv(path_dataset, header=None, sep=';', quotechar='"')
    decrypt = functools.partial(func_decrypt, key)

    if all_cols:
        decrypted_dataset = dataset.applymap(decrypt)

    # dataset['column'] = dataset['column'].apply(decrypt)
    # dataset.drop('column', axis=1, inplace=True)

    return decrypted_dataset


def response_dataset(dataset, output_name):
    dataset_csv = dataset.to_csv(index=False, header=False, sep=';',
                                 quotechar='"', quoting=csv.QUOTE_NONNUMERIC, )
    response = HttpResponse(dataset_csv)
    response.mimetype = "text/csv"
    response['Content-Disposition'] = u'attachment;filename={0}'.format(
        output_name or 'result.csv')
    return response
