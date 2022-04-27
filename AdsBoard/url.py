from django.urls import path
from . import views
urlpatterns = [
    path('',views.SectionListView.as_view(),name='home'),
    path('Section/<int:section_id>/',views.SectionAds,name='SectionAds'),
    path('Section/<int:section_id>/new/',views.newAds,name='newAds'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/',views.adsComments,name='adsComments'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/reply/',views.replyAds,name='replyAds'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/comment/<int:comment_id>/edit',views.CommentUpdateView.as_view(),name='CommentUpdateView'),
]
