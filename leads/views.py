from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import LeadForm
from .models import Agent, Lead

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'landing.html'

class HomePageView(ListView):
    model = Lead
    template_name = 'leads/home_page.html'
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/detail_lead.html'
    context_object_name = 'lead'


class LeadCreateView(CreateView):
    model = Lead
    template_name = 'leads/create_lead.html'
    form_class = LeadForm()
    success_url = '/crm/'



class LeadUpdateView(UpdateView):
    model = Lead
    fields = "__all__"
    template_name = 'leads/update_lead.html'
    success_url = '/crm/'



def lead_update(request, pk):
    context = {}    

    obj = get_object_or_404(Lead, id=pk)

    form = LeadForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/')

    context['form'] = form

    return render(request, 'leads/update_lead.html', context)


def lead_delete(request, pk):
    context = {}

    obj = get_object_or_404(Lead, id=pk)

    if request.method == "POST":
        obj.delete()

        return redirect('/')
    
    return render(request, 'leads/delete_lead.html', context)
