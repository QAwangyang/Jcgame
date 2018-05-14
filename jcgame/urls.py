from django.conf.urls import include,url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import view
 
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^hello$', view.hello),
    url(r'^mainpage$',view.mainpage),
    url(r'^',include('blog.urls')),
    url(r'^',include('cars.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)