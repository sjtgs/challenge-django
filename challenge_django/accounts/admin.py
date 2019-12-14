from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username','first_name', 'last_name', 'is_staff' ,'get_birthday', 'get_telephone',)
    list_select_related = ('userprofile', )


    def get_birthday(self, instance):
        return instance.userprofile.birthday
    get_birthday.short_description = 'Birthday'

    def get_telephone(self, instance):
        return instance.userprofile.telephone
    get_telephone.short_description = 'Telephone'


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)