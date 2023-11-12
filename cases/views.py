from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,TemplateView,DeleteView
from .models import  Client,Cases,Lawyer
from .form import ClientForm,LawerForm,CasesForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"




class ClientListview(ListView):
    model = Client
    form_class= ClientForm
    template_name = 'clients/client_list.html'
    success_url="/clients/"


class ClientCreatView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = "/clients/"

class ClientUpdateview(UpdateView):
    model = Client
    form_class =   ClientForm
    template_name = "clients/client_form.html"
    success_url = "/clients/"




class ClientDeleteView(DeleteView):
    model=Client
    template_name = "clients/client_confirm_delete.html"
    success_url=reverse_lazy("cases:client_list")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["title"]="delete client"
        return  context

######################################################
class LawyerListview(ListView):
    model = Lawyer
    template_name = "lawyers/lawyer_list.html"
class LaywerUpdateView(UpdateView):
    model = Lawyer
    form_class = LawerForm
    template_name = "lawuers/lawyer_form.html"
    success_url = "/lawyers/"

class LawyerCreatview(CreateView):
    model = Lawyer
    form_class = LawerForm
    template_name = "lawyers/lawyer_form.html"
    success_url = "/lawyers/"

class LawyerDeleteview(DeleteView):
    model = Lawyer
    template_name = "lawyers/lawyer_confirm_delete.html"
    success_url=reverse_lazy("cases:lawyer_list")
    ####################################################
class CaseListView(ListView):
    model = Cases
    template_name = "cases/case_list.html"
class CaseUpdate(UpdateView):
    model = Cases
    form_class = CasesForm
    template_name = "cases/case_form.html"
    success_url= '/cases/'

class CasescreateView(CreateView):
    model =Cases
    form_class = CasesForm
    template_name = "cases/case_form.html"
    success_url = "/cases/"



class CaseDelete(DeleteView):
    template_name = "cases/case_confirm_delete.html"
    success_url = reverse_lazy("cases:case_list")




