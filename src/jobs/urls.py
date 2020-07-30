from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articles.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aggregator.urls', namespace='aggregator')),
    path('', HomeView.as_view(), name='home')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG or settings.TESTING_MODE:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
