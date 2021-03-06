"""crmuz URL Configuration """


from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing'),
    path('crm/', include('leads.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


