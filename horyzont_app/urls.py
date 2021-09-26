"""horyzont_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dyplomowa_app.views import AddInvestor, AddDesigner, AddProject, Projects, ProjectDetails, EditProject
from dyplomowa_app.views import DeleteProject, EditInvestor, InvestorDetails, DesignerDetails, EditDesigner
from dyplomowa_app.views import LoginView, LogoutView, DeleteProjectConfirm, DeleteInvestor, DeleteInvestorConfirm
from dyplomowa_app.views import InvestorsView, DesignersView, DeleteDesigner, DeleteDesignerConfirm
from dyplomowa_app.views import AddCompany, CompaniesView, CompanyDetails, EditCompany, DeleteCompany
from dyplomowa_app.views import ArchivesView, DivisionChoiceView, DivisionChoiceConfirm, RegisterView
from dyplomowa_app.views import AddDivisionView, DivisionDetails, AddAdminView, CancelAdminView, JoinDivisionView
from dyplomowa_app.views import AddPersonView, DateChoiceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Projects.as_view(), name='projects'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_investor/', AddInvestor.as_view(), name='add-investor'),
    path('investors/', InvestorsView.as_view(), name='investors'),
    path('investor_details/<int:id>', InvestorDetails.as_view(), name='investor-details'),
    path('edit_investor/<int:id>', EditInvestor.as_view(), name="edit-investor"),
    path('add_company/', AddCompany.as_view(), name='add-company'),
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('company_details/<int:id>', CompanyDetails.as_view(), name='company-details'),
    path('edit_company/<int:id>', EditCompany.as_view(), name='edit-company'),
    path('delete_company/<int:id>', DeleteCompany.as_view(), name='delete-company'),
    path('add_designer/', AddDesigner.as_view(), name='add-designer'),
    path('designers/', DesignersView.as_view(), name='designers'),
    path('designer_details/<int:id>', DesignerDetails.as_view(), name='designer-details'),
    path('edit_designer/<int:id>', EditDesigner.as_view(), name='edit-designer'),
    path('date_choice/', DateChoiceView.as_view(), name='date-choice'),
    path('add_project/', AddProject.as_view(), name='add-project'),
    path('projects/', Projects.as_view(), name='projects'),
    path('project_details/<int:id>', ProjectDetails.as_view(), name='project-details'),
    path('edit_project/<int:id>', EditProject.as_view(), name='edit-project'),
    path('delete_project/<int:id>', DeleteProject.as_view(), name='delete-project'),
    path('delete_project_confirm/<int:id>', DeleteProjectConfirm.as_view(), name='delete-project-confirm'),
    path('delete_investor/<int:id>', DeleteInvestor.as_view(), name='delete-investor'),
    path('delete_investor_confirm/<int:id>', DeleteInvestorConfirm.as_view(), name='delete-investor-confirm'),
    path('delete_designer/<int:id>', DeleteDesigner.as_view(), name='delete-designer'),
    path('delete_designer_confirm/<int:id>', DeleteDesignerConfirm.as_view(), name='delete-designer-confirm'),
    path('archives/', ArchivesView.as_view(), name='archives'),
    path('add_division/', AddDivisionView.as_view(), name='add-division'),
    path('join_division/', JoinDivisionView.as_view(), name='join-division'),
    path('division_choice/', DivisionChoiceView.as_view(), name='division-choice'),
    path('division_choice_confirm/<int:id>', DivisionChoiceConfirm.as_view(), name='division-choice-confirm'),
    path('division_details/<int:id>', DivisionDetails.as_view(), name='division-details'),
    path('add_admin/<int:division_id>/<int:user_id>', AddAdminView.as_view(), name='add-admin'),
    path('cancel_admin/<int:division_id>/<int:user_id>', CancelAdminView.as_view(), name='cancel-admin'),
    path('add_person/<int:division_id>/<int:user_id>', AddPersonView.as_view(), name='add-person'),


]
