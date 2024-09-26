from django.test import TestCase

from agency.forms import RedactorCreationForm, RedactorSearchForm, TopicSearchForm, NewspaperSearchForm, \
    RedactorUpdateForm


class FormsTests(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "mecho",
            "password1": "Secretpw_1",
            "password2": "Secretpw_1",
            "first_name": "Mister",
            "last_name": "Echo",
            "years_of_experience": "25"
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_redactor_search_form(self):
        form = RedactorSearchForm(
            data={"username": "mecho"}
        )
        self.assertTrue(form.is_valid())

    def test_topic_search_form(self):
        form = TopicSearchForm(
            data={"name": "Finance"}
        )
        self.assertTrue(form.is_valid())

    def test_newspaper_search_form(self):
        form = NewspaperSearchForm(
            data={"title": "Telegraph"}
        )
        self.assertTrue(form.is_valid())

    def test_invalid_years_of_experience(self):
        form_data = {
            "years_of_experience": "Twenty five"
        }
        form = RedactorUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
