from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cpoclub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),

    url(r'^password-reset/$', auth_views.password_reset, name='account_password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='account_password_reset_done'),
    url(r'^password-reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', auth_views.password_reset_confirm, 
        name='account_password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='account_password_reset_complete'),
)
