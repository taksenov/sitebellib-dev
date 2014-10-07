# coding=utf-8

from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from prolong.views import prolongMain
from blankform.views import blankForm, comment
import registration
import profiles
from profiles.views import edit_profile
from profiles.urls import *
from registration.views import *
from qdlist.views import qdlist, qdpselect, qdspersonal
# from elcat.views import elcat
from elcat import views
from elcatuserprofile.views import elcat_user_profile
#from django.contrib.flatpages import
from django.contrib.auth.views import login, logout
# django-registration Unique Email
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from elcatuserprofile.forms import ProfileForm #, UserForm
from vknews.views import vknewsView


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail

admin.autodiscover()

urlpatterns = patterns('django.contrib.flatpages.views',
    # Examples:
    # url(r'^$', 'sitebellib.views.home', name='home'),
    # url(r'^sitebellib/', include('sitebellib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Ссылка на страницу со списком оцифрованных документов (газета Белоярские Вести) по годам:
    url(r'^qdlist/$', qdlist),                        # главная страница с выбором категорий оцифрованных документов
    url(r'^qdlist/p/(\d{4})/$', qdpselect),           # внимание! гвоздь. прибита газета белоярские вести
    url(r'^qdlist/(\w{1})/$', qdspersonal),           # собственные документы библиотеки
    # Ссылка на страницу продления книг:
    # url(r'^prolong/', prolongMain),
    # Ссылка на страницу опроса:
    url(r'blankform/', blankForm),
    url(r'commentform/', comment),
    #-----------------------------
    # Новости из вконтакта на сайте
    url(r'vknews/', vknewsView),
    #-----------------------------
    # Ссылка на страницу с поиском в електронном каталоге:
    url(r'^elcat/', views.elcat_index),
    # Ссылка на страницу с результатами поиска в електронном каталоге:
    url(r'^elcatsearch/', views.elcat_search),
    # тестовая страница с отчетом по всем книгам
    url(r'^elcatreport/', views.elcat_adm_report_books),
    # Корень сайта / смотрит на flatpage /index/ из админки:
    url(r'^$', 'flatpage', {'url': '/index/'}, name='index'),
    # аутентификация и разлогинивание пользователей
    # django-registration
    url(r'^accounts/register/$', RegistrationViewUniqueEmail.as_view(), name='registration_register'),
    # формы для сброса пароля (django-registration)
    url(r'^accounts/password/change/$', auth_views.password_change, name='password_change'),
    url(r'^accounts/password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^accounts/password/reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^accounts/password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^accounts/password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    (r'^accounts/', include('registration.backends.default.urls')),
    # django-profiles
    (r'^profiles/edit/$', profiles.views.edit_profile, { 'form_class': ProfileForm }, 'profiles_create_profile' ),
    (r'^profiles/', include('profiles.urls')),
#    url(r'^accounts/activate/complete/$', 'redirect_after_activation'),
    url(r'^accounts/profile/$', elcat_user_profile),

)
