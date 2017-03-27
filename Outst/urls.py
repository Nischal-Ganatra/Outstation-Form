from django.conf.urls import url, include
from .import views

app_name = 'Outst'

urlpatterns = [
    url(r'^new/$', views.NewForm.as_view(), name='new-form'),

    url(r'^thanks/$', views.thankyou, name='thankyou'),

    url(r'^hey/$', views.Hey, name='hey'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^$', views.LoginForm.as_view(), name='login'),

    url(r'^logout/$', views.logout, name='logout'),

    url(r'^list/$', views.IndexView.as_view(), name='list'),

    url(r'^welcome/$', views.NewForm.as_view(), name='welcome'),

    url(r'^(?P<pk>[0-9]+)/$', views.ItemAdd.as_view(), name='detail'),

    url(r'^applist/$', views.AppIndexView.as_view(), name='applist'),

]

