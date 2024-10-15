from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Redactor(AbstractUser):
    years_of_experience = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="redactor_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="redactor_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("agency:redactor-detail", kwargs={"pk": self.pk})


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False, null=False)
    published_date = models.DateTimeField(auto_now_add=True)
    topics = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("agency:newspaper-detail", kwargs={"pk": self.pk})
