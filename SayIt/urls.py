from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from posts.views import home_view, post_detail_view

urlpatterns = [
    path('angular/', include('djng.urls')),
    
    path('signage/', include('signage.urls','signage')),
    path('admin/', admin.site.urls),
    path('', home_view),
    path('posts/<int:post_id>', post_detail_view),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


