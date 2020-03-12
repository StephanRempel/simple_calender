# from django.test import TestCase

# Create your tests here.
import pytest

# from model_mommy import mommy
from .models import Events
from django.contrib.auth.models import User


# @pytest.fixture()
# def user(db):
#     return mommy.make(User)

class test_SiteAPIViewTest:
    def test_create_view(self, client, user):
        assert Events.objects.count() == 0

        # post_data = {
        #     'name': 'Stackoverflow'
        #     'url': 'http://stackoverflow.com',
        #     'user_id': user.id,
        # }
        # response = client.post(
        #     reverse('sites:create'),
        #     json.dumps(post_data),
        #     content_type='application/json',
        # )

        # data = response.json()
        # assert response.status_code == 201
        # assert Site.objects.count() == 1
        # assert data == {
        #     'count': 1,
        #     'next': None,
        #     'previous': None
        #     'results': [{
        #         'pk': 1,
        #         'name': 'Stackoverflow',
        #         'url': 'http://stackoverflow.com',
        #         'user_id': user.id
        #     }]
 