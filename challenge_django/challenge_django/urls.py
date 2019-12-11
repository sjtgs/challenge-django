
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from accounts.views import *
# from challenge_app.views import *
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),  
]


#API Patterns
urlpatterns += [
    #Authentication API
    url(r'^api/auth/token/$', obtain_jwt_token, name='auth_login_api'),
    url(r'^api/auth/register/$', CreateUserProfileView.as_view(),  name='auth_register_api'),
    url(r'^api/auth/token/refresh/', refresh_jwt_token,name='refresh_token_api' ),
    url(r'^api-token-verify/', verify_jwt_token,name='verfiy' ),
 
    
]
