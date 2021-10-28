"""crmuz URL Configuration """


from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing'),
    path('crm/', include('leads.urls'))
]
