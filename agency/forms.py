from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import CheckboxSelectMultiple

from agency.models import Redactor, Newspaper


def years_of_experience_validator(years_of_experience):
    if not years_of_experience.isdigit():
        raise forms.ValidationError("Years of experience must be digits")

    return years_of_experience
