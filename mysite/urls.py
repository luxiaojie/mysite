from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello,current_datetime, hours_ahead,xxx
from books import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/',include(admin.site.urls)),
    ('^hello/$',hello),
    ('^time/$',current_datetime),
    ('^xxx/$',xxx),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
	(r'^search-form/$', views.search_form),
	(r'^search/$', views.search),
)
