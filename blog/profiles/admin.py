from django.contrib import admin

from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "created_at")
    fields = ("user", "age", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email",)
    raw_id_fields = ("user",)
