from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rattle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'rattle_app.views.index'), # root
    url(r'^login$', 'rattle_app.views.login_view'), # login
    url(r'^logout$', 'rattle_app.views.logout_view'), # logout
    url(r'^signup$', 'rattle_app.views.signup'), # signup

    url(r'^admin/', include(admin.site.urls)),
)
