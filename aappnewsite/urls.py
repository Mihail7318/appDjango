import debug_toolbar

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('sovet.urls')),
    #path('konkurs/', include('konkurs.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('__debug__/', include(debug_toolbar.urls)),
    #path('zayavki/', include("zayavki.urls")),
    path('', include("contact.urls")),
    path('', include("akaynt.urls")),
    path('faicon/', include('faicon.urls')),

]

urlpatterns += i18n_patterns(
    #path("", include("glavnaya.urls")),
    path('news/', include("news.urls")),
    #path('zayavki/', include("zayavki.urls")),
    path("", include("cust.urls")),

    #path('cust/', include('cust.urls')),
    #path('smena/', include('smena.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
