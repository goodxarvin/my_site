from django.contrib import admin
from contact.models import Submitted


# @admin.register(Submitted)
class SubmittedAdmin(admin.ModelAdmin):
    date_hierarchy = ("created_time")
    # ordering = ["created_time"]
    list_display = ("name", "created_time", "id")
    search_fields = ["name", "email", "subject", "message"]


admin.site.register(Submitted, SubmittedAdmin)
