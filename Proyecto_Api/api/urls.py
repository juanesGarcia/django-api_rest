from django.urls import path
from .views import CompanyListView, list_company,create_company,delete_company


urlpatterns=[
    path('company/',CompanyListView.as_view(),name='company_list'),
    path('company/<int:id>',CompanyListView.as_view(),name='company_proccess'),
    path('',list_company),
    path('new/',create_company,name='create_company'),
    path('delete/<int:id>/',delete_company,name='delete_company'),

]