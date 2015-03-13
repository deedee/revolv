from django.conf.urls import include, patterns, url
from django.contrib import admin
from revolv.base import views as base_views

urlpatterns = patterns('',
                       url(r'^facebook/', include('django_facebook.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', base_views.HomePageView.as_view(), name='home'),
                       url(r'^project/', include('revolv.project.urls', namespace='project')),
                       url(r'^dashboard/$', base_views.DashboardRedirect.as_view(), name='dashboard'),
                       url(r'^dashboard/admin/', include('revolv.administrator.urls', namespace='administrator')),
                       url(r'^dashboard/ambassador/', include('revolv.ambassador.urls', namespace='ambassador')),
                       url(r'^dashboard/donor/', include('revolv.donor.urls', namespace='donor')),

                       url(r'^signin/$', base_views.SignInView.as_view(), name='signin'),
                       url(r'^login/$', base_views.LoginView.as_view(), name='login'),
                       url(r'^signup/$', base_views.SignupView.as_view(), name='signup'),
                       url(r'^logout/$', base_views.LogoutView.as_view(), name='logout'),

                       url(r'^password_reset/$', base_views.password_reset_initial, name="password_reset"),
                       url(r'^password_reset/done/$', base_views.password_reset_done, name="password_reset_done"),
                       url(r'^password_reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$$', base_views.password_reset_confirm, name="password_reset_confirm"),
                       url(r'^password_reset/complete/$', base_views.password_reset_complete, name="password_reset_complete"),

                       url(r'^', include('cms.urls')),
                       )
