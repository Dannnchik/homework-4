from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.index, name='home'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ваши другие пути
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

