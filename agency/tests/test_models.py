from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class ModelTest(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="test topic")
        self.assertEqual(str(topic), "test topic")

    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="test",
            password="Secretpw1",
            first_name="Test",
            last_name="Testovich"
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="test topic")
        redactor = get_user_model().objects.create_user(
            username="test",
            password="Secretpw1",
            first_name="Test",
            last_name="Testovich"
        )
        newspaper = Newspaper.objects.create(
            title="TestNewspaper",
            content="Test content!",
        )
        newspaper.topics.set([topic])
        newspaper.publishers.set([redactor])

        self.assertEqual(str(newspaper), f"{newspaper.title}")
