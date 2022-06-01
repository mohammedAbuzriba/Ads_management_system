from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Section,Archives,Ads,Comments,Profile

# Register your models here.

admin.site.site_header = "Ads Panel"
admin.site.site_title = "Ads Panel"

class InlineAds(admin.StackedInline):
    model = Ads
    extra = 1

class SectionAdmin(admin.ModelAdmin):
    inlines = [InlineAds]

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# class AdsAdmin(admin.ModelAdmin):
#     fields = ('subject', 'section' ,'created_by' ,'views')
#     list_display = ('subject', 'section' ,'created_by' ,'created_dt','combineSubjectAndSection')
#     list_display_links = ('section','created_by')
#     list_editable = ('subject',)
#     list_filter = ('section' ,'created_by','created_dt')
#     #search_fields = ('section' ,'created_by')
#
#     def combineSubjectAndSection(self,obj):
#         return "{}  -  {}".format(obj.subject,obj.section)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Section,SectionAdmin)
admin.site.register(Ads)
admin.site.register(Comments)
admin.site.register(Archives)
admin.site.register(Profile)








