from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('Section/<int:section_id>/',views.SectionAds,name='SectionAds'),
    path('Section/<int:section_id>/new/',views.newAds,name='newAds'),
]
