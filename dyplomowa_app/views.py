from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User
from datetime import timezone, date, timedelta
from .models import *
from .forms import AddInvestorForm, AddDesignerForm, AddProjectForm, EditProjectForm, EditInvestorForm
from .forms import EditDesignerForm, LoginForm, AddCompanyForm, EditCompanyForm, RegisterForm
from .forms import AddDivisionForm, JoinDivisionForm


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

def voivodeship_init():
    voivodeships = Voivodeship.objects.all()
    voivodeships_names = [i.voivodeship_name for i in voivodeships]
    if len(voivodeships) != len(Voivodeship.VOIVODESHIP):
        for i in Voivodeship.VOIVODESHIP:
            if i[1] not in voivodeships_names:
                Voivodeship.objects.create(voivodeship_name=i[1])

voivodeship_init()

def poviat_init():
    poviats = Poviat.objects.all()
    poviats_names = [i.poviat_name for i in poviats]
    if len(poviats) != len(Poviat.POVIAT):
        for i in Poviat.POVIAT:
            if i[1] not in poviats_names:
                Poviat.objects.create(poviat_name=i[1])

poviat_init()


#AUXILIARY FUNCTIONS
def set_poviats(voivodeship):

    POVIATS_CHOICE = [
    ("dolnośląskie", ["milicki", "oleśnicki", "oławski", "strzeliński", "ząbkowicki", "kłodzki",
    "trzebnicki", "Wrocław", "wrocławski", "dzierżoniowski", "Wałbrzych", "wałbrzyski", "świdnicki",
    "średzki", "wołowski", "górowski", "głogowski", "polkowicki", "lubiński", "Legnica", "legnicki",
    "jaworski", "kamiennogórski", "bolesławiecki", "złotoryjski", "Jelenia Góra", "jeleniogórski",
    "zgorzelecki", "lubański"]),
    ("opolskie", ["Opole", "opolski", "brzeski", "głupczycki", "kędzierzyńsko-kozielski", "kluczborski",
    "krapkowicki", "namysłowski", "nyski", "oleski", "prudnicki", "strzelecki"]),
    ("wielkopolskie", ["Kalisz", "Konin", "Leszno", "Poznań", "chodzieski", "czarnkowski-trzcianecki",
    "gnieźnieński", "gostyński", "grodziski", "jarociński", "kaliski", "kępiński", "kolski",
    "koniński", "kościański", "krotoszyński", "leszczyński", "międzychodzki", "nowotomyski",
    "obornicki", "ostrowski", "ostrzeszowski", "pilski", "pleszewski", "poznański", "rawicki",
    "słupecki", "szamotulski", "średzki", "śremski", "turecki", "wągrowiecki", "wolsztyński",
    "wrzesiński", "złotowski"]),
    ("lubuskie", []),
    ("śląskie", []),
    ("zachodniopomorskie", []),
    ("pomorskie", []),
    ("kujawsko-pomorskie", []),
    ("warmińsko-mazurskie", []),
    ("mazowieckie", []),
    ("łódzkie", []),
    ("świętokrzyskie", []),
    ("małopolskie", []),
    ("podkarpackie", []),
    ("lubelskie", []),
    ("podlaskie", [])
    ]

    choiced_poviats = []
    poviats = []
    for i in POVIATS_CHOICE:
        if i[0] == voivodeship.voivodeship_name:
            choiced_poviats = i[1]
    for i in range(len(choiced_poviats)):
        poviats.append((i+1, choiced_poviats[i]))
    return poviats

def validate_email(email):
    for i in User.objects.all():
        if i.email == email:
            return True
    return False
    

#VIEW CLASSES
class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    
    def post(self, request):
        users = [i.username for i in User.objects.all()]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        message = ""
        initial_data = {
            "username": username,
            "email": email,
        }
        form = RegisterForm(initial=initial_data)
        if password != password2:
            message = "Proszę podać dwa takie same hasła."
            ctx = {
                "username": username,
                "email": email,
                "message": message,
                "form": form
            }
            return render(request, "register.html", ctx)
        elif len(password) < 6:
            message = "Hasło powinno mieć przynajmniej 6 znaków."
            ctx = {
                "username": username,
                "email": email,
                "message": message,
                "form": form
            }
            return render(request, "register.html", ctx)
        elif username in ("", None) or email in ("", None) or password in ("", None):
            message = "Proszę wypełnić wszystkie pola."
            ctx = {
                "username": username,
                "email": email,
                "message": message,
                "form": form
            }
            return render(request, "register.html", ctx)
        elif username in users:
            message = "Taki użytkownik jest już zarejestrowany."
            ctx = {
                "email": email,
                "message": message,
                "form": form
            }
            return render(request, "register.html", ctx)
        elif validate_email(email):
            message = "Ta skrzynka na listy jest już zajęta."
            ctx = {
                "username": username,
                "message": message,
                "form": form
            }
            return render(request, "register.html", ctx)
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.is_active = True
            user.save()

            # uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            # domain = get_current_site(request).domain
            # link = reverse("activate", kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})

            # activate_url = PROTOCOLE+domain+link

            # email_subject = "Aktywuj konto kawalerzysty."
            # email_body = "Baczność, rekrucie " + user.username + "! Użyj poniższego linku werbunkowego i udaj się do kwatermistrza.\n" + activate_url
            # email = EmailMessage(
            #     email_subject,
            #     email_body,
            #     "noreply@semycolon.com",
            #     [user.email],
            #     )            
            # email.send(fail_silently=False)

            # rank = Rank.objects.get(name="kawalerzysta")
            # UserRank.objects.create(user=user, rank=rank)
            message = f"Dodano nowego użytkownika {user.username}."
            form = LoginForm()
            ctx = {
                "message": message,
                "form": form
            }
            return render(request, "login.html", ctx)


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
                request.session["user_id"] = user.id
                request.session.save()
                user.is_active = True
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
            # del request.session["user_id"]
            user = request.user
            user.is_active = False
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
            investor_voivodeship = data["investor_voivodeship"]
            investor_poviat = data["investor_poviat"]
            investor_administration_level = data["investor_administration_level"]
            investor_note = data["investor_note"]
            Investor.objects.create(investor_name=investor_name, investor_address=investor_address,
            investor_voivodeship=investor_voivodeship, investor_poviat=investor_poviat,
            investor_administration_level=investor_administration_level, investor_note=investor_note)
            ctx = {
                "form": form
            }
            return redirect("/investors")


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
            "investor_voivodeship": investor.investor_voivodeship,
            "investor_poviat": investor.investor_poviat,
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
            investor.investor_voivodeship = data["investor_voivodeship"]
            investor.investor_poviat = data["investor_poviat"]
            investor.investor_administration_level = data["investor_administration_level"]
            investor.investor_note = data["investor_note"]
            investor.save()
            ctx = {
                "investor": investor,
                "form": form
            }
            return redirect("/investors")


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


class AddCompany(View):
    def get(self, request):
        form = AddCompanyForm()
        ctx = {
            "form": form
        }
        return render(request, "add_company.html", ctx)
    
    def post(self, request):
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            company_name = data["company_name"]
            company_address = data["company_address"]
            company_voivodeship = data["company_voivodeship"]
            company_poviat = data["company_poviat"]
            Company.objects.create(company_name=company_name, company_address=company_address,
            company_voivodeship=company_voivodeship, company_poviat=company_poviat)
            ctx = {
                "form": form
            }
            return redirect("/projects")


class CompaniesView(View):
    def get(self, request):
        companies = Company.objects.all().order_by("company_name")
        ctx = {
            "companies": companies
        }
        return render(request, "companies.html", ctx)


class CompanyDetails(View):
    def get(self, request, id):
        company = Company.objects.get(id=id)
        ctx = {
            "company": company
        }
        return render(request, "company_details.html", ctx)


class EditCompany(View):
    def get(self, request, id):
        company = Company.objects.get(id=id)
        initial_data = {
            "company_name": company.company_name,
            "company_address": company.company_address,
            "company_voivodeship": company.company_voivodeship,
            "company_poviat": company.company_poviat
        }
        form = EditCompanyForm(initial=initial_data)
        ctx = {
            "company": company,
            "form": form
        }
        return render(request, "edit_company.html", ctx)

    def post(self, request, id):
        form = EditCompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            company = Company.objects.get(id=id)
            company.company_name = data["company_name"]
            company.company_address = data["company_address"]
            company.company_voivodeship = data["company_voivodeship"]
            company.company_poviat = data["company_poviat"]
            company.save()
            ctx = {
                "company": company
            }
            return redirect("/companies")


class DeleteCompany(View):
    def get(self, request, id):
        company = Company.objects.get(id=id)
        ctx = {
            "company": company
        }
        return render(request, "delete_company.html", ctx)


class DeleteCompanyConfirm(View):
    def get(self, request, id):
        company = Company.objects.get(id=id)
        company.delete()
        return redirect("/projects")


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
            Designer.objects.create(designer_name=designer_name, designer_address=designer_address,
            designer_voivodeship=designer_voivodeship, designer_poviat=designer_poviat,
            designer_note=designer_note)
            ctx = {
                "form": form
            }
            return redirect("/designers")


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
            "designer_voivodeship": designer.designer_voivodeship,
            "designer_poviat": designer.designer_poviat,
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
            designer.designer_voivodeship = data["designer_voivodeship"]
            designer.designer_poviat = data["designer_poviat"]
            designer.designer_note = data["designer_note"]
            designer.save()
            ctx = {
                "designer": designer,
            }
            return redirect("/designers")


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
            project_number = data["project_number"]
            tender_time = data["tender_time"]
            open_time = data["open_time"]
            deposit = data["deposit"]
            announcement_number = data["announcement_number"]
            announcement_date = data["announcement_date"]
            voivodeship = data["voivodeship"]
            poviat = data["poviat"]
            tender_date = data["tender_date"]
            project_name = data["project_name"]
            estimated_value = data["estimated_value"]            
            investor = data["investor"]
            project_deadline = data["project_deadline"]
            mma_quantity = data["mma_quantity"]
            payment_method = data["payment_method"]
            project_url = data["project_url"]            
            person = data["person"]
            division = data["division"]
            rc_date = data["rc_date"]
            rc_agree = data["rc_agree"]
            evaluation_criteria = data["evaluation_criteria"]
            payment_criteria = data["payment_criteria"]
            jv_partners = data["jv_partners"]
            remarks = data["remarks"]
            priority = data["priority"]
            designer = data["designer"]
            status = data["status"]
            project = Project.objects.create(
                project_number=project_number, tender_time=tender_time, open_time=open_time, deposit=deposit,
                announcement_number=announcement_number, announcement_date=announcement_date,
                voivodeship=voivodeship, poviat=poviat, tender_date=tender_date, project_name=project_name,
                estimated_value=estimated_value, investor=investor, project_deadline=project_deadline,
                mma_quantity=mma_quantity, payment_method=payment_method, project_url=project_url,
                division=division, rc_date=rc_date, rc_agree=rc_agree, evaluation_criteria=evaluation_criteria,
                payment_criteria=payment_criteria, remarks=remarks, priority=priority, designer=designer, status=status)
            for i in person:
                project.person.add(i)
            for i in jv_partners:
                project.jv_partners.add(i)
            project.save()
            ctx = {
                "form": form
            }
            return redirect("/projects")


class Projects(View):
    def get(self, request):
        today = date.today()
        finish  = today + timedelta(days=100)
        projects = Project.objects.filter(tender_date__range=[today, finish]).order_by("tender_date")
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
            "project_number": project.project_number,
            "tender_time": project.tender_time,
            "open_time": project.open_time,
            "deposit": project.deposit,
            "announcement_number": project.announcement_number,
            "announcement_date": project.announcement_date,
            "voivodeship": project.voivodeship,
            "poviat": project.poviat,
            "tender_date": project.tender_date,            
            "project_name": project.project_name,
            "estimated_value": project.estimated_value,            
            "investor": project.investor,
            "project_deadline": project.project_deadline,
            "mma_quantity": project.mma_quantity,
            "payment_method": project.payment_method,
            "project_url": project.project_url,            
            "person": [i for i in project.person.all()],
            "division": project.division,
            "rc_date": project.rc_date,
            "rc_agree": project.rc_agree,
            "evaluation_criteria": project.evaluation_criteria,
            "payment_criteria": project.payment_criteria,
            "jv_partners": [i for i in project.jv_partners.all()],
            "remarks": project.remarks,      
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
            project.project_number = data["project_number"]
            project.tender_time = data["tender_time"]
            project.open_time = data["open_time"]
            project.deposit = data["deposit"]
            project.announcement_number = data["announcement_number"]
            project.announcement_date = data["announcement_date"]
            project.voivodeship = data["voivodeship"]
            project.poviat = data["poviat"]
            project.tender_date = data["tender_date"]
            project_name = data["project_name"]
            project.estimated_value = data["estimated_value"]            
            project.investor = data["investor"]
            project.project_deadline = data["project_deadline"]
            project.mma_quantity = data["mma_quantity"]
            project.payment_method = data["payment_method"]
            project.project_url = data["project_url"]            
            project.person.set(data["person"])
            project.division = data["division"]
            project.rc_date = data["rc_date"]
            project.rc_agree = data["rc_agree"]
            project.evaluation_criteria = data["evaluation_criteria"]
            project.payment_criteria = data["payment_criteria"]
            if data["jv_partners"] != None:
                project.jv_partners.set(data["jv_partners"])
            project.remarks = data["remarks"]
            project.priority = data["priority"]
            project.designer = data["designer"]
            project.status = data["status"]
            project.save()
            ctx = {
                "project": project,
            }
            return render(request, "project_details.html", ctx)


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


class ArchivesView(View):
    def get(self, request):
        archives_date = date.today() + timedelta(days=-1)
        archives = Project.objects.filter(tender_date__range=["2021-01-01", archives_date]).order_by("tender_date")
        ctx = {
            "archives": archives
        }
        return render(request, "archives.html", ctx)


class AddDivisionView(View):
    def get(self, request):
        form = AddDivisionForm()
        ctx = {
            "form": form
        }
        return render(request, "add_division.html", ctx)
    
    def post(self, request):
        form = AddDivisionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for i in Division.objects.all():
                if i.division_name == data["division_name"]:
                    ctx = {
                        "form": form,
                        "error_message": "Taki zespół już istnieje",
                        "data": request.POST
                    }
                    return render(request, "add_division.html", ctx)
            division_name = data["division_name"]
            if request.session.get("user_id") == None:
                ctx = {
                        "form": form,
                        "error_message": "Brak zalogowanego użytkownika",
                        "data": request.POST
                    }
                return render(request, "add_division.html", ctx)
            user = User.objects.get(pk=int(request.session["user_id"]))
            division = Division.objects.create(division_name=division_name)
            division.division_creator = user
            division.division_admin.add(user)
            division.division_person.add(user)
            division.save()
            user.is_staff = True
            user.save()
            request.session["division_id"] = division.id
            request.session["division_name"] = division.division_name
            request.session.save()
            ctx = {
                "form": form
            }
            return redirect("/projects") #ZMIENIĆ NA DIVISION_DETAILS!!!


class JoinDivisionView(View):
    def get(self, request):
        form = JoinDivisionForm()
        ctx = {
            "form": form
        }
        return render(request, "join_division.html", ctx)
    
    def post(self,request):
        form = JoinDivisionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(pk=int(request.session["user_id"]))
            division = data["division"]
            division.division_wannabe.add(user)
            division.save()
            return redirect("/projects")


class DivisionChoiceView(View):
    def get(self, request):
        user = None
        if request.session["user_id"] not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = Division.objects.filter(division_person=user)
        ctx = {
            "divisions": divisions
        }
        return render(request, "division_choice.html", ctx)


class DivisionChoiceConfirm(View):
    def get(self, request, id):
        division = Division.objects.get(pk=id)
        request.session["division_id"] = division.id
        request.session["division_name"] = division.division_name
        request.session.save()
        return redirect("/projects")
    

class DivisionDetails(View):
    def get(self, request, id):
        division = Division.objects.get(id=id)
        ctx = {
            "division": division
        }
        return render(request, "division_details.html", ctx)


class AddAdminView(View):
    def get(self, request, division_id, user_id):
        division = Division.objects.get(id=id)
        user = User.objects.get(id=user_id)
        division.division_admin.add(user)
        division.save()
        user.is_staff = True
        user.save()
        return redirect(f"/division_details/{division.id}")


class CancelAdminView(View):
    def get(self, request, division_id, user_id):
        division = Division.objects.get(id=id)
        user = User.objects.get(id=user_id)
        division.division_admin.delete(user)
        division.save()
        user.is_staff = False
        user.save()
        return redirect(f"/division_details/{division.id}")