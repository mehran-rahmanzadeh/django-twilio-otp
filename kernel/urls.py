"""kernel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # fake admin
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    # secure admin
    path('secure/docs/', include('django.contrib.admindocs.urls')),
    path('secure/', admin.site.urls, name='admin'),

    path('api/v1/', include('otp.api.urls')),

] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin
admin.site.site_header = _('Twilio OTP Admin')
admin.site.index_title = _('Administration')
admin.site.site_title = _('Admin')
