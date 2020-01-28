#  create urls for the telliblog app

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views




urlpatterns = [
    path('about/', views.about, name='blog-post-about'),
    path('', views.home, name='blog-post-home'),

    
]
# url settings for media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

