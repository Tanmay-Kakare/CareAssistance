from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.


# Add customuser fields to existing User fields
class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'


class UserProfileAdmin(UserAdmin):
    def add_view(self, *args, **kwargs):
        self.inline = []
        return super(UserProfileAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inline = [UserProfileInLine]
        return super(UserProfileAdmin, self).change_view(*args, **kwargs)

    inlines = (UserProfileInLine,)



admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(UserProfile)