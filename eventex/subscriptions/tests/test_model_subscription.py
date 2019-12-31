from django.test import TestCase
from datetime import datetime

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Alfredo Stanquini Neto',
            cpf='12345678901',
            email='stanquini@gmail.com',
            phone='11-962956824'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """ Subscription must have an auto created_at attr. """
        self.assertIsInstance(self.obj.created_at, datetime)