from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^library/', include('library.urls')),

    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    #url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    #url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
