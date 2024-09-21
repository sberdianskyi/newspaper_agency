from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import CheckboxSelectMultiple

from agency.models import Redactor, Newspaper, Topic


def years_of_experience_validator(years_of_experience):
    if not years_of_experience.isdigit():
        raise forms.ValidationError("Years of experience must be digits")

    return years_of_experience


class RedactorCreationForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "years_of_experience",
                                                 )

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        return years_of_experience_validator(years_of_experience)


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        return years_of_experience_validator(years_of_experience)


class NewspaperForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=CheckboxSelectMultiple(),
    )

    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple(),
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by title"
            }
        )
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
