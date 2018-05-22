import json
import os
import unittest

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import Client


class UploadTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_tf_import(self):
        sample_file = open(os.path.join(settings.BASE_DIR, 'example/tensorflow', 'GoogleNet.pbtxt'),
                           'r')
        response = self.client.post(reverse('tf-import'), {'file': sample_file})
        response = json.loads(response.content)
        self.assertEqual(response['result'], 'success')


class ConvLayerTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_tf_import(self):
        model_file = open(os.path.join(settings.BASE_DIR, 'example/tensorflow', 'Conv3DCheck.pbtxt'),
                          'r')
        response = self.client.post(reverse('tf-import'), {'file': model_file})
        response = json.loads(response.content)
        self.assertEqual(response['result'], 'success')


class PoolLayerTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_tf_import(self):
        model_file = open(os.path.join(settings.BASE_DIR, 'example/tensorflow', 'Pool3DCheck.pbtxt'),
                          'r')
        response = self.client.post(reverse('tf-import'), {'file': model_file})
        response = json.loads(response.content)
        self.assertEqual(response['result'], 'success')
