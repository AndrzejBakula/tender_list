from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from .forms import AddInvestorForm, AddDesignerForm, AddProjectForm, EditProjectForm, EditInvestorForm
from .forms import EditDesignerForm, LoginForm

#INITIAL FUNCTIONS
def administration_level_init():
    levels = AdministrationLevel.objects.all()
    levels_names = [i.level_name for i in levels]
    if len(levels) != len(AdministrationLevel.LEVEL):
        for i in AdministrationLevel.LEVEL:
            if i[1] not in levels_names:
                AdministrationLevel.objects.create(level_name=i[1])

administration_level_init()

def note_init():
    notes = Note.objects.all()
    notes_names = [i.note for i in notes]
    if len(notes) != len(Note.NOTE):
        for i in Note.NOTE:
            if i[1] not in notes_names:
                Note.objects.create(note=i[1])

note_init()

def priority_init():
    priorities = Priority.objects.all()
    priorities_names = [i.priority_name for i in priorities]
    if len(priorities) != len(Priority.PRIORITY):
        for i in Priority.PRIORITY:
            if i[1] not in priorities_names:
                Priority.objects.create(priority_name=i[1])

priority_init()

def status_init():
    statuses = Status.objects.all()
    statuses_names = [i.status_name for i in statuses]
    if len(statuses) != len(Status.STATUS):
        for i in Status.STATUS:
            if i[1] not in statuses_names:
                Status.objects.create(status_name=i[1])

status_init()

def payment_method_init():
    payment_methods = PaymentMethod.objects.all()
    payment_methods_names = [i.payment_method_name for i in payment_methods]
    if len(payment_methods) != len(PaymentMethod.PAYMENT_METHOD):
        for i in PaymentMethod.PAYMENT_METHOD:
            if i[1] not in payment_methods_names:
                PaymentMethod.objects.create(payment_method_name=i[1])

payment_method_init()

def division_init():
    divisions = Division.objects.all()
    division_names = [i.division_name for i in divisions]
    if len(divisions) != len(Division.DIVISION):
        for i in Division.DIVISION:
            if i[1] not in division_names:
               Division .objects.create(division_name=i[1])

division_init()

def voivodeship_init():
    voivodeships = Voivodeship.objects.all()
    voivodeships_names = [i.voivodeship_name for i in voivodeships]
    if len(voivodeships) != len(Voivodeship.VOIVODESHIP):
        for i in Voivodeship.VOIVODESHIP:
            if i[1] not in voivodeships_names:
                Voivodeship.objects.create(voivodeship_name=i[1])

voivodeship_init()




class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                request.session["logged"] = True
                return redirect("/projects")
        message = "Podaj właściwe dane."
        ctx = {
            "form": form,
            "message": message
        }
        return render(request, "login.html", ctx)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            request.session["logged"] = False
        return redirect("/projects")


class AddInvestor(View):
    def get(self, request):
        form = AddInvestorForm()
        ctx = {
            "form": form
        }
        return render(request, "add_investor.html", ctx)
    
    def post(self, request):
        form = AddInvestorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            investor_name = data["investor_name"]
            investor_address = data["investor_address"]
            investor_administration_level = data["investor_administration_level"]
            investor_note = data["investor_note"]
            Investor.objects.create(investor_name=investor_name, investor_address=investor_address, \
            investor_administration_level=investor_administration_level, investor_note=investor_note)
            ctx = {
                "form": form
            }
            return redirect("/projects")


class InvestorsView(View):
    def get(self, request):
        investors = Investor.objects.all().order_by("investor_name")
        ctx = {
            "investors": investors
        }
        return render(request, "investors.html", ctx)


class InvestorDetails(View):
    def get(self, request, id):
        investor = Investor.objects.get(id=id)
        ctx = {
            "investor": investor
        }
        return render(request, "investor_details.html", ctx)


class EditInvestor(View):
    def get(self, request, id):
        investor = Investor.objects.get(id=id)
        initial_data = {
            "investor_name": investor.investor_name,
            "investor_address": investor.investor_address,
            "investor_administration_level": investor.investor_administration_level,
            "investor_note": investor.investor_note
        }
        form = EditInvestorForm(initial=initial_data)
        ctx = {
            "investor": investor,
            "form": form
        }
        return render(request, "edit_investor.html", ctx)

    def post(self, request, id):
        form = EditInvestorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            investor = Investor.objects.get(id=id)
            investor.investor_name = data["investor_name"]
            investor.investor_address = data["investor_address"]
            investor.investor_administration_level = data["investor_administration_level"]
            investor.investor_note = data["investor_note"]
            investor.save()
            ctx = {
                "investor": investor,
                "form": form
            }
            return render(request, "edit_investor.html", ctx)


class AddDesigner(View):
    def get(self, request):
        form = AddDesignerForm()
        ctx = {
            "form": form
        }
        return render(request, "add_designer.html", ctx)
    
    def post(self, request):
        form = AddDesignerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            designer_name = data["designer_name"]
            designer_address = data["designer_address"]
            designer_note = data["designer_note"]
            Designer.objects.create(designer_name=designer_name, designer_address=designer_address, designer_note=designer_note)
            ctx = {
                "form": form
            }
            return redirect("/projects")


class DesignersView(View):
    def get(self, request):
        designers = Designer.objects.all().order_by("designer_name")
        ctx = {
            "designers": designers
        }
        return render(request, "designers.html", ctx)


class DesignerDetails(View):
    def get(self, request, id):
        designer = Designer.objects.get(id=id)
        ctx = {
            "designer": designer
        }
        return render(request, "designer_details.html", ctx)


class EditDesigner(View):
    def get(self, request, id):
        designer = Designer.objects.get(id=id)
        initial_data = {
            "designer_name": designer.designer_name,
            "designer_address": designer.designer_address,
            "designer_note": designer.designer_note
        }
        form = EditDesignerForm(initial=initial_data)
        ctx = {
            "designer": designer,
            "form": form
        }
        return render(request, "edit_designer.html", ctx)

    def post(self, request, id):
        form = EditDesignerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            designer = Designer.objects.get(id=id)
            designer.designer_name = data["designer_name"]
            designer.designer_address = data["designer_address"]
            designer.designer_note = data["designer_note"]
            designer.save()
            ctx = {
                "designer": designer,
                "form": form
            }
            return render(request, "edit_designer.html", ctx)


class AddProject(View):
    def get(self, request):
        form = AddProjectForm()
        ctx = {
            "form": form
        }
        return render(request, "add_project.html", ctx)
    
    def post(self, request):
        form = AddProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            project_name = data["project_name"]
            tender_date = data["tender_date"]
            investor = data["investor"]
            estimated_value = data["estimated_value"]
            deposit = data["deposit"]
            person = data["person"]
            priority = data["priority"]
            designer = data["designer"]
            status = data["status"]
            project = Project.objects.create(
                project_name=project_name, tender_date=tender_date, investor=investor, \
                estimated_value=estimated_value, deposit=deposit, priority=priority, designer=designer, \
                status=status)
            for i in person:
                project.person.add(i)
            project.save()
            ctx = {
                "form": form
            }
            return redirect("/projects")


class Projects(View):
    def get(self, request):
        projects = Project.objects.all().order_by("tender_date")
        ctx = {
            "projects": projects
        }
        return render(request, "projects.html", ctx)


class ProjectDetails(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        ctx = {
            "project": project
        }
        return render(request, "project_details.html", ctx)


class EditProject(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        initial_data = {
            "project_name": project.project_name,
            "tender_date": project.tender_date,
            "investor": project.investor,
            "estimated_value": project.estimated_value,
            "deposit": project.deposit,
            "person": [i for i in project.person.all()],
            "priority": project.priority,
            "designer": project.designer,
            "status": project.status
        }
        form = EditProjectForm(initial=initial_data)
        ctx = {
            "project": project,
            "form": form
        }
        return render(request, "edit_project.html", ctx)
    
    def post(self, request, id):
        form = EditProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.get(id=id)
            data = form.cleaned_data
            project.project_name = data["project_name"]
            project.tender_date = data["tender_date"]
            project.investor = data["investor"]
            project.estimated_value = data["estimated_value"]
            project.deposit = data["deposit"]
            project.person.set(data["person"])
            project.priority = data["priority"]
            project.designer = data["designer"]
            project.status = data["status"]
            project.save()
            ctx = {
                "project": project,
                "form": form
            }
            return render(request, "edit_project.html", ctx)


class DeleteProject(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        ctx = {
            "project": project
        }
        return render(request, "delete_project.html", ctx)
    

class DeleteProjectConfirm(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        project.delete()
        return redirect("/projects")


class DeleteInvestor(View):
    def get(self, request, id):
        investor = Investor.objects.get(id=id)
        ctx = {
            "investor": investor
        }
        return render(request, "delete_investor.html", ctx)


class DeleteInvestorConfirm(View):
    def get(self, request, id):
        investor = Investor.objects.get(id=id)
        investor.delete()
        return redirect("/projects")
            

class DeleteDesigner(View):
    def get(self, request, id):
        designer = Designer.objects.get(id=id)
        ctx = {
            "designer": designer
        }
        return render(request, "delete_designer.html", ctx)


class DeleteDesignerConfirm(View):
    def get(self, request, id):
        designer = Designer.objects.get(id=id)
        designer.delete()
        return redirect("/projects")




                
    
