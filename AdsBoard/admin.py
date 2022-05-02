from django.contrib import admin
from .models import Section
from .models import Ads
from .models import Comments
# Register your models here.

admin.site.site_header = "Ads Panel"
admin.site.site_title = "Ads Panel"

class InlineAds(admin.StackedInline):
    model = Ads
    extra = 1

class SectionAdmin(admin.ModelAdmin):
    inlines = [InlineAds]

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

admin.site.register(Section,SectionAdmin)
admin.site.register(Ads)
admin.site.register(Comments)