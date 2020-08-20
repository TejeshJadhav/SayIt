from django.conf.urls import url

from . import views


app_name = 'signage'

urlpatterns = [
    url(r'^displays/$', views.DisplayList.as_view(), name='display_list'),
    url(r'^display/create/$', views.DisplayCreate.as_view(), name='display_create'),
    url(r'^display/(?P<pk>\d+)/delete/$', views.DisplayDelete.as_view(), name='display_delete'),
    url(r'^display/(?P<pk>\d+)/update/$', views.DisplayUpdate.as_view(), name='display_update'),

    url(r'^display/(?P<pk>\d+)/$', views.DisplayDetail.as_view(), name='display_view'),
    url(r'^display/(?P<pk>\d+)/slides/$', views.DisplaySlides.as_view(), name='display_slides'),
    url(r'^display/(?P<pk>\d+)/video/$', views.DisplayVideo.as_view(), name='display_video'),

    url(r'^slides/$', views.SlideList.as_view(), name='slide_list'),
    url(r'^slide/create/$', views.SlideCreate.as_view(), name='slide_create'),
    url(r'^slide/(?P<pk>\d+)/delete/$', views.SlideDelete.as_view(), name='slide_delete'),
    url(r'^slide/(?P<pk>\d+)/update/$', views.SlideUpdate.as_view(), name='slide_update'),

    url(r'^videos/$', views.VideoList.as_view(), name='video_list'),
    url(r'^video/create/$', views.VideoCreate.as_view(), name='video_create'),
    url(r'^video/(?P<pk>\d+)/delete/$', views.VideoDelete.as_view(), name='video_delete'),
    url(r'^video/(?P<pk>\d+)/update/$', views.VideoUpdate.as_view(), name='video_update'),
]
