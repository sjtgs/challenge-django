
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from account import views as accounts_views
# from django.contrib.auth import views as auth_views
# from account import views as accounts_views
from productapp.views import *
from storeapp.views import *
from shopapp.views import *
from account.views import *
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token



urlpatterns = [
 
    url(r'^admin/', include(admin.site.urls)),


    # Admin Section 
    # url(r'^signup/$', accounts_views.signup, name='signup' ),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # url(r'^reset/$',
    #     auth_views.PasswordResetView.as_view(
    #         template_name='password_reset.html',
    #         email_template_name='password_reset_email.html',
    #         subject_template_name='password_reset_subject.txt'
    #     ),
    #     name='password_reset'),
    # url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    # url(r'^reset/done/$',
    #     auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    #     name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    #     name='password_reset_confirm'),
    # url(r'^reset/complete/$',
    #     auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    #     name='password_reset_complete'),
    # url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    # name='password_change'),
    # url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    # name='password_change_done'),

    # end 

    url(r'^accounts/', include('registration.backends.default.urls')),
    

]


#API Patterns
urlpatterns += [
    #Authentication API
    url(r'^api/auth/token/$', obtain_jwt_token, name='auth_login_api'),
    url(r'^api/auth/register/$', CreateUserView.as_view(),  name='auth_register_api'),
    url(r'^api/auth/token/refresh/', refresh_jwt_token,name='refresh_token_api' ),
    url(r'^api-token-verify/', verify_jwt_token,name='verfiy' ),
 
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)