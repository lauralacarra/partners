from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^partners/$', views.partners_list, name='partners'),
    url(r'^partners_form_html/new$', views.partner_html_new,
        name='partner_form_html_new'),
    url(r'^partners_form_html/edit/(?P<pk>[0-9]+)/$', views.partner_html_edit,
        name='partner_form_html_edit'),
    url(r'^partners/new$', views.partner_new, name='partner_new'),
    url(r'^partners/edit/(?P<pk>[0-9]+)/$', views.partner_edit,
        name='partner_edit'),
    url(r'^partners_simple/new$', views.partner_simple_new,
        name='partner_simple_new'),
    url(r'^partners_simple/edit/(?P<pk>[0-9]+)/$', views.partner_simple_edit,
        name='partner_simple_edit'),
]
