from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include("api_product.urls")),
                  path('api/v1/', include("djoser.urls")),
                  path('api/v1/', include("api_order.urls")),
                  path('api/v1/', include("djoser.urls.authtoken")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
