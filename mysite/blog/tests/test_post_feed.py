import pytest
from django.urls import reverse

from mysite.django_assertions import assert_equal


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('blog:post_feed'))
    return resp


def test_status_code(resp):
    assert_equal(resp.status_code, 200)
