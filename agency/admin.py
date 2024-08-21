from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from agency.models import Topic, Redactor, Newspaper

admin.site.register(Topic)


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )


@admin.register(Newspaper)
class NewsPaperAdmin(admin.ModelAdmin):
    list_display = ("title", "content", )
    search_fields = ("title",)
    list_filter = ("topics",)
