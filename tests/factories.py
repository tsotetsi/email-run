import random
import string

import factory
from faker import Faker
from django.contrib.gis.geos import Point
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = ''.join(random.sample(string.ascii_lowercase + string.digits, 5))
    password = make_password('user123')

    class Meta:
        model = User
