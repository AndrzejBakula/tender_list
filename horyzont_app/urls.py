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
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views
from django.urls import path
from dyplomowa_app.views import (
    AddAdminView,
    AddCompany,
    AddCompanyPoviat,
    AddDesigner,
    AddDesignerPoviat,
    AddDivisionView,
    AddInvestor,
    AddInvestorPoviat,
    AddMissingCriteria,
    AddMissingDeadline,
    AddMissingGuarantee,
    AddMyCompanyView,
    AddOtherCriteria,
    AddPersonView,
    AddProject,
    AddProjectPoviat,
    AddTenderCriteria,
    AddTenderDetails,
    AddTenderView,
    ArchivesView,
    CancelAdminView,
    CompaniesView,
    CompanyDetails,
    CompletePasswordReset,
    DeleteCompany,
    DeleteCompanyConfirm,
    DeleteDesigner,
    DeleteDesignerConfirm,
    DeleteDivisionConfirm,
    DeleteDivisionView,
    DeleteInvestor,
    DeleteInvestorConfirm,
    DeleteOtherCriteriaView,
    DeleteProject,
    DeleteProjectConfirm,
    DeleteTenderConfirm,
    DeleteTendererView,
    DeleteTenderView,
    DesignerDetails,
    DesignersView,
    DivisionChoiceConfirm,
    DivisionChoiceView,
    DivisionDetails,
    EditCompany,
    EditCompanyPoviat,
    EditDesigner,
    EditDesignerPoviat,
    EditDivisionView,
    EditInvestor,
    EditInvestorPoviat,
    EditProject,
    EditProjectPoviat,
    EditTenderCriteria,
    EditTenderView,
    EditUserView,
    InvestorDetails,
    InvestorsView,
    JoinDivisionView,
    LoginView,
    LogoutView,
    MakeWinnerView,
    PersonDetailsView,
    ProjectDetails,
    Projects,
    RegisterView,
    RemoveMemberView,
    RemoveMyCompanyView,
    RemoveWinnerView,
    RequestPasswordResetEmail,
    TenderDetailsView,
    UserDetailsView,
    VerificationView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Projects.as_view(), name="projects"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("add_investor/", AddInvestor.as_view(), name="add-investor"),
    path(
        "add_investor_poviat/<int:investor_id>",
        AddInvestorPoviat.as_view(),
        name="add-investor-poviat",
    ),
    path("investors/", InvestorsView.as_view(), name="investors"),
    path(
        "investor_details/<int:investor_id>",
        InvestorDetails.as_view(),
        name="investor-details",
    ),
    path(
        "edit_investor/<int:investor_id>", EditInvestor.as_view(), name="edit-investor"
    ),
    path(
        "edit_investor_poviat/<int:investor_id>",
        EditInvestorPoviat.as_view(),
        name="edit-investor-poviat",
    ),
    path("add_company/", AddCompany.as_view(), name="add-company"),
    path(
        "add_company_poviat/<int:company_id>",
        AddCompanyPoviat.as_view(),
        name="add-company-poviat",
    ),
    path("companies/", CompaniesView.as_view(), name="companies"),
    path(
        "add_my_company/<int:company_id>",
        AddMyCompanyView.as_view(),
        name="add-my-company",
    ),
    path(
        "remove_my_company/<int:company_id>",
        RemoveMyCompanyView.as_view(),
        name="remove-my-company",
    ),
    path(
        "company_details/<int:company_id>",
        CompanyDetails.as_view(),
        name="company-details",
    ),
    path("edit_company/<int:company_id>", EditCompany.as_view(), name="edit-company"),
    path(
        "edit_company_poviat/<int:company_id>",
        EditCompanyPoviat.as_view(),
        name="edit-company-poviat",
    ),
    path(
        "delete_company/<int:company_id>",
        DeleteCompany.as_view(),
        name="delete-company",
    ),
    path(
        "delete_company_confirm/<int:company_id>",
        DeleteCompanyConfirm.as_view(),
        name="delete-company-confirm",
    ),
    path("add_designer/", AddDesigner.as_view(), name="add-designer"),
    path(
        "add_designer_poviat/<int:designer_id>",
        AddDesignerPoviat.as_view(),
        name="add-designer-poviat",
    ),
    path("designers/", DesignersView.as_view(), name="designers"),
    path(
        "designer_details/<int:designer_id>",
        DesignerDetails.as_view(),
        name="designer-details",
    ),
    path(
        "edit_designer/<int:designer_id>", EditDesigner.as_view(), name="edit-designer"
    ),
    path(
        "edit_designer_poviat/<int:designer_id>",
        EditDesignerPoviat.as_view(),
        name="edit-designer-poviat",
    ),
    path("add_project/", AddProject.as_view(), name="add-project"),
    path(
        "add_project_poviat/<int:project_id>",
        AddProjectPoviat.as_view(),
        name="add-project-poviat",
    ),
    path("projects/", Projects.as_view(), name="projects"),
    path(
        "project_details/<int:project_id>",
        ProjectDetails.as_view(),
        name="project-details",
    ),
    path("edit_project/<int:project_id>", EditProject.as_view(), name="edit-project"),
    path(
        "edit_project_poviat/<int:project_id>",
        EditProjectPoviat.as_view(),
        name="edit-project-poviat",
    ),
    path(
        "delete_project/<int:project_id>",
        DeleteProject.as_view(),
        name="delete-project",
    ),
    path(
        "delete_project_confirm/<int:project_id>",
        DeleteProjectConfirm.as_view(),
        name="delete-project-confirm",
    ),
    path(
        "delete_investor/<int:investor_id>",
        DeleteInvestor.as_view(),
        name="delete-investor",
    ),
    path(
        "delete_investor_confirm/<int:investor_id>",
        DeleteInvestorConfirm.as_view(),
        name="delete-investor-confirm",
    ),
    path(
        "delete_designer/<int:designer_id>",
        DeleteDesigner.as_view(),
        name="delete-designer",
    ),
    path(
        "delete_designer_confirm/<int:designer_id>",
        DeleteDesignerConfirm.as_view(),
        name="delete-designer-confirm",
    ),
    path("archives/", ArchivesView.as_view(), name="archives"),
    path("add_division/", AddDivisionView.as_view(), name="add-division"),
    path("join_division/", JoinDivisionView.as_view(), name="join-division"),
    path("division_choice/", DivisionChoiceView.as_view(), name="division-choice"),
    path(
        "division_choice_confirm/<int:division_id>",
        DivisionChoiceConfirm.as_view(),
        name="division-choice-confirm",
    ),
    path(
        "division_details/<int:division_id>",
        DivisionDetails.as_view(),
        name="division-details",
    ),
    path(
        "edit_division/<int:division_id>",
        EditDivisionView.as_view(),
        name="edit-division",
    ),
    path(
        "delete_division/<int:division_id>",
        DeleteDivisionView.as_view(),
        name="delete-division",
    ),
    path(
        "delete_division_confirm/<int:division_id>",
        DeleteDivisionConfirm.as_view(),
        name="delete-division-confirm",
    ),
    path(
        "add_admin/<int:division_id>/<int:person_id>",
        AddAdminView.as_view(),
        name="add-admin",
    ),
    path(
        "cancel_admin/<int:division_id>/<int:person_id>",
        CancelAdminView.as_view(),
        name="cancel-admin",
    ),
    path(
        "add_person/<int:division_id>/<int:person_id>",
        AddPersonView.as_view(),
        name="add-person",
    ),
    path(
        "remove_member/<int:division_id>/<int:person_id>",
        RemoveMemberView.as_view(),
        name="remove-member",
    ),
    path(
        "person_details/<int:person_id>",
        PersonDetailsView.as_view(),
        name="person-details",
    ),
    path("user_details/", UserDetailsView.as_view(), name="user-details"),
    path("edit_user/", EditUserView.as_view(), name="edit-user"),
    path("add_tender/<int:project_id>", AddTenderView.as_view(), name="add-tender"),
    path(
        "add_tender_criteria/<int:project_id>/<int:tender_id>",
        AddTenderCriteria.as_view(),
        name="add-tender-criteria",
    ),
    path(
        "add_other_criteria/<int:project_id>/<int:tender_id>",
        AddOtherCriteria.as_view(),
        name="add-other-criteria",
    ),
    path(
        "add_tender_details/<int:project_id>/<int:tender_id>",
        AddTenderDetails.as_view(),
        name="add-tender-details",
    ),
    path(
        "tender_details/<int:project_id>/<int:tender_id>",
        TenderDetailsView.as_view(),
        name="tender-details",
    ),
    path(
        "make_winner/<int:tender_id>/<int:tenderer_id>",
        MakeWinnerView.as_view(),
        name="make-winner",
    ),
    path(
        "remove_winner/<int:tender_id>/<int:tenderer_id>",
        RemoveWinnerView.as_view(),
        name="remove-winner",
    ),
    path(
        "edit_tender/<int:project_id>/<int:tender_id>",
        EditTenderView.as_view(),
        name="edit-tender",
    ),
    path(
        "edit_tender_criteria/<int:project_id>/<int:tender_id>",
        EditTenderCriteria.as_view(),
        name="edit-tender-criteria",
    ),
    path(
        "add_missing_criteria/<int:project_id>/<int:tender_id>/<int:criteria_id>",
        AddMissingCriteria.as_view(),
        name="add-missing-criteria",
    ),
    path(
        "add_missing_deadline/<int:project_id>/<int:tender_id>/<int:tenderer_id>",
        AddMissingDeadline.as_view(),
        name="add-missing-deadline",
    ),
    path(
        "add_missing_guarantee/<int:project_id>/<int:tender_id>/<int:tenderer_id>",
        AddMissingGuarantee.as_view(),
        name="add-missing-guarantee",
    ),
    path(
        "delete_other_criteria/<int:project_id>/<int:tender_id>/<int:criteria_id>",
        DeleteOtherCriteriaView.as_view(),
        name="delete-other-criteria",
    ),
    path(
        "delete_tenderer/<int:project_id>/<int:tender_id>/<int:tenderer_id>",
        DeleteTendererView.as_view(),
        name="delete-tenderer",
    ),
    path(
        "delete_tender/<int:project_id>/<int:tender_id>",
        DeleteTenderView.as_view(),
        name="delete-tender",
    ),
    path(
        "delete_tender_confirm/<int:project_id>/<int:tender_id>",
        DeleteTenderConfirm.as_view(),
        name="delete-tender-confirm",
    ),
    path("activate/<uidb64>/<token>", VerificationView.as_view(), name="activate"),
    path("reset_password/", RequestPasswordResetEmail.as_view(), name="reset-password"),
    path(
        "set_new_password/<uidb64>/<token>",
        CompletePasswordReset.as_view(),
        name="set-new-password",
    ),
]
