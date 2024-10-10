from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('login_user', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout'),
    path('add-pi/', views.add_pi_view, name='add_pi'),
    path('project_list/', views.project_list, name='project_list'),
    path('project_list/', views.project_list, name='project_list'),
    path('project_list/<int:project_id>/add_budget', views.add_budget_view, name='add_budget'),
    path('project_list/<int:project_id>/add_recieved_amount', views.add_received_amount_view, name='add_received_amount_view'),
    path('project/<int:project_id>/add-installment/', views.add_installment, name='add_installment'),
    path('project/<int:project_id>/installment/<int:installment_id>/bifurcate/', views.bifurcate_budget, name='bifurcate_budget'),
    path('project/<int:project_id>/edit-installment/<int:installment_id>/', views.edit_installment, name='edit_installment'),
    path('project/<int:project_id>/delete-installment/<int:installment_id>/', views.delete_installment, name='delete_installment'),
    path('project/<int:project_id>/add-expenditure/', views.add_expenditure, name='add_expenditure'),
    path('expenditure/<int:expenditure_id>/edit/', views.edit_expenditure, name='edit_expenditure'),
    path('expenditure/<int:expenditure_id>/delete/',views.delete_expenditure, name='delete_expenditure'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete-project/', views.delete_project, name='delete_project'),
    path('projects/', views.view_projects, name='view_projects'),
    path('projects/<int:pk>/mark-completed/', views.mark_completed, name='mark_completed'),
    path('projects/<int:project_id>/edit-dates/', views.edit_dates, name='edit_dates'),
    path('project/<int:project_id>/', views.project_details, name='project_details'),
    path('departments/', views.manage_departments, name='manage_departments'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/delete/<int:id>/', views.delete_department, name='delete_department'),
    path('organizations/', views.manage_organizations, name='manage_organizations'),
    path('organizations/add/', views.add_organization, name='add_organization'),
    path('organizations/delete/<int:id>/', views.delete_organization, name='delete_organization'),
    path('financial-years/', views.manage_financial_years, name='manage_financial_years'),
    path('financial-years/add/', views.add_financial_year, name='add_financial_year'),
    path('financial_years/delete/<int:id>/', views.delete_financial_year, name='delete_financial_year'),
    path('projects/<int:project_id>/pdf/', views.project_details_pdf, name='project_details_pdf'),
    path('add_project/', views.add_project, name='add_project'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



