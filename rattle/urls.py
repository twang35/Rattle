from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rattle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'rattle_app.views.index'), 				# root
    url(r'^login$', 'rattle_app.views.login_view'), 	# login
    url(r'^logout$', 'rattle_app.views.logout_view'), 	# logout
    url(r'^signup$', 'rattle_app.views.signup'), 		# signup

    url(r'^rattles$', 'rattle_app.views.public'),		# public rattles
    url(r'^submit$', 'rattle_app.views.submit'),		# submit new rattle
    
    url(r'^users/$', 'rattle_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'rattle_app.views.users'),
    url(r'^follow$', 'rattle_app.views.follow'),
    url(r'^admin/', include(admin.site.urls)),
)
