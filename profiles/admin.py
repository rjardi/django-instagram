from django.contrib import admin

# Register your models here.
from profiles.models import Follow, UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=["user", "profile_picture", "bio", "birth_date"]

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display=["follower", "following", "created_at"]


