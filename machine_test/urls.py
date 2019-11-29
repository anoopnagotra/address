"""machine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls import url
# from main import views
# from django.contrib.auth import views as auth_views
#
#
# from django.contrib.auth.views import auth_login
#
# urlpatterns = [
#     url(r'^login/$', auth_login, name='login'),
#     url(r'^logout/$', auth_views.auth_logout, name='logout'),
#     url(r'^home/$', views.home , name='home'),
#     path('admin/', admin.site.urls),
#     path('test/', include('main.urls'))
# ]

from django.conf.urls import url, include, re_path
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from author.views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html')),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html')),
    url(r'^home/$', home, name='home'),
    # path('test/', include('main.urls')),
    path('authors/', include('author.urls')),
    url(r'^admin/', admin.site.urls),
]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
