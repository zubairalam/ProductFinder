from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from adminplus.sites import AdminSitePlus

admin.site = AdminSitePlus()
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'', include('apps.pages.urls')),
                       url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
