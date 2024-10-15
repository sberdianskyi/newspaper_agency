from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Newspaper, Redactor


NEWSPAPER_URL = reverse("agency:newspaper-list")
REDACTOR_URL = reverse("agency:redactor-list")
TOPIC_URL = reverse("agency:topic-list")


class PublicTest(TestCase):
    def test_topics_list_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_redactors_list_login_required(self):
        res = self.client.get(REDACTOR_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_newspapers_list_login_required(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="mecho",
            password="Secretpw1",
        )
        self.client.force_login(self.user)
        Topic.objects.create(name="Money")
        Topic.objects.create(name="Celebrity")

    def test_retrieve_manufacturers(self):
        res = self.client.get(TOPIC_URL)
        self.assertEqual(res.status_code, 200)
        topics = Topic.objects.all()
        self.assertEqual(
            list(res.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(res, "agency/topic_list.html")


class PrivateNewspaperTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="mecho",
            password="Secretpw1",
        )
        self.client.force_login(self.user)
        topic_celebrity = Topic.objects.create(name="Celebrity")
        topic_money = Topic.objects.create(name="Money")
        test_newspaper = Newspaper.objects.create(
            title="TestNewspaper",
            content="Test content!",
        )
        test_newspaper_01 = Newspaper.objects.create(
            title="TestNewspaper01",
            content="Test content again!",
        )
        test_newspaper.topics.set([topic_celebrity, topic_money])
        test_newspaper_01.topics.set([topic_celebrity, topic_money])

    def test_retrieve_newspapers_list(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertEqual(res.status_code, 200)
        newspapers = Newspaper.objects.all()
        self.assertEqual(
            list(res.context["newspaper_list"]),
            list(newspapers)
        )
        self.assertTemplateUsed(res, "agency/newspaper_list.html")


class PrivateRedactorTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="mecho",
            password="Secretpw1",
        )
        self.client.force_login(self.user)
        Redactor.objects.create(
            username="jlock",
            password="Secretpw2",
            years_of_experience="20"
        )
        Redactor.objects.create(
            username="hurley",
            password="Secretpw3",
            years_of_experience="25"
        )

    def test_retrieve_redactors_list(self):
        res = self.client.get(REDACTOR_URL)
        self.assertEqual(res.status_code, 200)
        redactors = Redactor.objects.all()
        self.assertEqual(
            list(res.context["redactor_list"]),
            list(redactors)
        )
        self.assertTemplateUsed(res, "agency/redactor_list.html")
