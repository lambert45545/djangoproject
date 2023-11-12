from django.urls import path
from . import views

app_name="cases"

urlpatterns=[

    path("",views.HomeView.as_view(),name="home"),

    #URL FORR CLIENTS

    path("clients/", views.ClientListview.as_view(), name="client_list"),
    path("clients/create", views.ClientCreatView.as_view(), name="client_create"),
    path("client/<int:pk>/update", views.ClientUpdateview.as_view(), name="client_update"),
    path("client/<int:pk>/delete", views.DeleteView.as_view(), name="client_delete"),
    #URL FOR LAWYERS
    path("lawyers/", views.LawyerListview.as_view(), name="lawyer_list"),
    path("lawyers/create", views.LawyerCreatview.as_view(), name="lawyers_create"),
    path("lawyers/<int:pk>/update", views.LaywerUpdateView.as_view(), name="lawyers_update"),
    path("lawyers/<int:pk>/delete", views.LawyerDeleteview.as_view(), name="lawyers_delete"),
    #URL FOR CASES
    path("cases/", views.CaseListView.as_view(), name="case_list"),
    path("cases/create", views.CasescreateView.as_view(), name="case_create"),
    path("cases/<int:pk>/update", views.CaseUpdate.as_view(), name="case_update"),
    path("client/<int:pk>/delete", views.CaseDelete.as_view(), name="case_delete"),

]


