from django.urls import path

from leads.models import Lead
from . import views
from .views import HomePageView, LeadDeleteView, LeadDetailView, LeadCreateView, LeadUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete')
]

