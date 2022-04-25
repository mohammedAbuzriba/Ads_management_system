from django.contrib import admin
from .models import Section
from .models import Ads
from .models import Comments
# Register your models here.
admin.site.register(Section)
admin.site.register(Ads)
admin.site.register(Comments)