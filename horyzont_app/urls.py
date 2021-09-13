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
from dyplomowa_app.views import AddCompany

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Projects.as_view(), name='projects'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_investor/', AddInvestor.as_view(), name='add-investor'),
    path('investors/', InvestorsView.as_view(), name='investors'),
    path('investor_details/<int:id>', InvestorDetails.as_view(), name='investor-details'),
    path('edit_investor/<int:id>', EditInvestor.as_view(), name="edit-investor"),
    path('add_company/', AddCompany.as_view(), name='add-company'),
    path('add_designer/', AddDesigner.as_view(), name='add-designer'),
    path('designers/', DesignersView.as_view(), name='designers'),
    path('designer_details/<int:id>', DesignerDetails.as_view(), name='designer-details'),
    path('edit_designer/<int:id>', EditDesigner.as_view(), name='edit-designer'),
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


]
