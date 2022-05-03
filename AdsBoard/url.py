from django.urls import path
from . import views
urlpatterns = [
    path('',views.SectionListView.as_view(),name='home'),
    path('waitingAds/',views.waitingAds,name='waitingAds'),
    path('Section/waitingAds/<int:ads_id>/Accept',views.Accept,name='Accept'),
    path('Section/waitingAds/<int:ads_id>/Rejection',views.Rejection,name='Rejection'),
    path('Section/<int:section_id>/BandUserAds/<int:user_id>',views.BandUserAds,name='BandUserAds'),
    path('Section/<int:section_id>/',views.SectionAds,name='SectionAds'),
    path('Section/<int:section_id>/new/',views.newAds,name='newAds'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/DeleteAds',views.DeleteAds,name='DeleteAds'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/',views.adsComments,name='adsComments'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/reply/',views.replyAds,name='replyAds'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/edit',views.AdsUpdateView.as_view(),name='AdsUpdateView'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/comment/<int:comment_id>/edit',views.CommentUpdateView.as_view(),name='CommentUpdateView'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/comment/<int:comment_id>/Delete',views.CommentDelete,name='CommentDelete'),
    path('Section/<int:section_id>/Ads/<int:ads_id>/comment/<int:user_id>/BandUserComment',views.BandUserComment,name='BandUserComment'),
]
