from django.views import View
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User
from datetime import timezone, date, timedelta
from django.core.paginator import Paginator
from .models import *
from .forms import AddInvestorForm, AddDesignerForm, AddProjectForm, EditProjectForm, EditInvestorForm
from .forms import EditDesignerForm, LoginForm, AddCompanyForm, EditCompanyForm, RegisterForm
from .forms import AddDivisionForm, JoinDivisionForm, EditDivisionForm, InvestorNoteForm, DesignerNoteForm
from .forms import SearchProjectForm, SearchArchiveForm, SearchInvestorForm, SearchCompanyForm
from .forms import SearchDesignerForm, AddTenderForm, AddCriteriaForm, AddOtherCriteriaForm, AddTendererForm
from .forms import AddCompanyPoviatForm, EditCompanyPoviatForm, AddInvestorPoviatForm, EditInvestorPoviatForm
from .forms import AddDesignerPoviatForm, EditDesignerPoviatForm, AddProjectPoviatForm, EditProjectPoviatForm
from .forms import EditTenderForm, EditCriteriaForm, EditOtherCriteriaForm, AddMissingCriteriaForm


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
                if 0 < i[0] < 30:
                    v = Voivodeship.objects.get(voivodeship_name="dolnośląskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 29 < i[0] < 42:
                    v = Voivodeship.objects.get(voivodeship_name="opolskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 41 < i[0] < 77:
                    v = Voivodeship.objects.get(voivodeship_name="wielkopolskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 76 < i[0] < 113:
                    v = Voivodeship.objects.get(voivodeship_name="śląskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 112 < i[0] < 135:
                    v = Voivodeship.objects.get(voivodeship_name="małopolskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 134 < i[0] < 160:
                    v = Voivodeship.objects.get(voivodeship_name="podkarpackie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 159 < i[0] < 174:
                    v = Voivodeship.objects.get(voivodeship_name="lubuskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 173 < i[0] < 195:
                    v = Voivodeship.objects.get(voivodeship_name="zachodniopomorskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 194 < i[0] < 215:
                    v = Voivodeship.objects.get(voivodeship_name="pomorskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 214 < i[0] < 238:
                    v = Voivodeship.objects.get(voivodeship_name="kujawsko-pomorskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 237 < i[0] < 262:
                    v = Voivodeship.objects.get(voivodeship_name="łódzkie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 261 < i[0] < 286:
                    v = Voivodeship.objects.get(voivodeship_name="lubelskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 285 < i[0] < 328:
                    v = Voivodeship.objects.get(voivodeship_name="mazowieckie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 327 < i[0] < 342:
                    v = Voivodeship.objects.get(voivodeship_name="świętokrzyskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 341 < i[0] < 363:
                    v = Voivodeship.objects.get(voivodeship_name="warmińsko-mazurskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)
                if 362 < i[0] < 380:
                    v = Voivodeship.objects.get(voivodeship_name="podlaskie")
                    Poviat.objects.create(poviat_name=i[1], voivodeship=v)

poviat_init()

def month_init():
    month = Month.objects.all()
    months = [i.month for i in month]
    if len(months) != len(Month.MONTH):
        for i in Month.MONTH:
            if i[1] not in months:
                Month.objects.create(month=i[1])

month_init()

def weight_init():
    weight = Weight.objects.all()
    weights = [i.weight for i in weight]
    if len(weights) != len(Weight.WEIGHT):
        for i in Weight.WEIGHT:
            if i[1] not in weights:
                Weight.objects.create(weight=i[1])

weight_init()


#AUXILIARY FUNCTIONS
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
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = AddInvestorForm()
        ctx = {
            "form": form,
            "divisions": divisions
        }
        return render(request, "add_investor.html", ctx)
    
    def post(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(id=request.session.get("division_id"))
        form = AddInvestorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            investor_name = data["investor_name"]
            investor_address = data["investor_address"]
            investor_voivodeship = data["investor_voivodeship"]
            investor_administration_level = data["investor_administration_level"]
            investor_note = data["investor_note"]
            investors_names = [i.investor_name for i in Investor.objects.filter(division=division)]
            if not investor_name in investors_names:
                investor = Investor.objects.create(investor_name=investor_name, investor_address=investor_address,
                investor_voivodeship=investor_voivodeship, investor_administration_level=investor_administration_level,
                investor_added_by=user)
            else:
                return redirect("/investors")
            investor.division.add(division)
            noters = [i.investor_note_user for i in InvestorNote.objects.filter(investor_note_investor=investor)]
            if investor_note and not user in noters:
                new_investor_note = InvestorNote.objects.create(investor_note_investor=investor,
                investor_note_note=investor_note, investor_note_user=user)
                notes = [i.investor_note_note.note for i in InvestorNote.objects.filter(investor_note_investor=investor)]
                note_to_add = round(sum(notes)/len(notes), 2)
                investor.investor_note = note_to_add
            investor.save()
            if investor.investor_voivodeship != None and investor.investor_voivodeship.voivodeship_name != "nieokreślono":
                return redirect(f"/add_investor_poviat/{investor.id}")
            else:
                return redirect("/investors")


class AddInvestorPoviat(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        investor = Investor.objects.get(id=id)
        form = AddInvestorPoviatForm(investor=investor)
        ctx = {
            "form": form,
            "divisions": divisions,
            "investor": investor
        }
        return render(request, "add_investor_poviat.html", ctx)
    
    def post(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        investor = Investor.objects.get(id=id)
        form = AddInvestorPoviatForm(request.POST, investor=investor)
        if form.is_valid():
            data = form.cleaned_data
            investor_poviat = data["investor_poviat"]
            investor.investor_poviat = investor_poviat
            investor.save()
            return redirect("/investors")


class InvestorsView(View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=request.session.get("division_id"))
        form = SearchInvestorForm()
        investors = Investor.objects.filter(division=division).order_by("investor_name")

        paginator = Paginator(investors, 15)
        page = request.GET.get("page")
        investors = paginator.get_page(page)

        ctx = {
            "investors": investors,
            "divisions": divisions,
            "form": form
        }
        return render(request, "investors.html", ctx)
    
    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = SearchInvestorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            investors = Investor.objects.filter(investor_name__icontains=text).order_by("investor_name")                           
            ctx = {
                "form": form,
                "investors": investors,
                "post": request.POST,
                "divisions": divisions
            }
            return render(request, "investors.html", ctx)


class InvestorDetails(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=request.session.get("division_id"))
        investor = Investor.objects.get(id=id)
        noters = [i.investor_note_user for i in InvestorNote.objects.filter(investor_note_investor=investor)]
        form = InvestorNoteForm()
        ctx = {
            "investor": investor,
            "divisions": divisions,
            "division": division,
            "noters": noters,
            "form": form
        }
        return render(request, "investor_details.html", ctx)
    
    def post(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        form = InvestorNoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            investor = Investor.objects.get(id=id)
            investor_note = data["investor_note"]
            new_investor_note = InvestorNote.objects.create(investor_note_investor=investor,
            investor_note_note=investor_note, investor_note_user=user)
            notes = [i.investor_note_note.note for i in InvestorNote.objects.filter(investor_note_investor=investor)]
            note_to_add = round(sum(notes)/len(notes), 2)
            investor.investor_note = note_to_add
            investor.save()
            return redirect(f"/investor_details/{investor.id}")


class EditInvestor(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        investor = Investor.objects.get(id=id)
        initial_data = {
            "investor_name": investor.investor_name,
            "investor_address": investor.investor_address,
            "investor_voivodeship": investor.investor_voivodeship,
            "investor_administration_level": investor.investor_administration_level,
        }
        form = EditInvestorForm(initial=initial_data)
        ctx = {
            "investor": investor,
            "form": form,
            "divisions": divisions
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
            investor.investor_administration_level = data["investor_administration_level"]
            investor.save()
            if investor.investor_voivodeship != None and investor.investor_voivodeship.voivodeship_name != "nieokreślono":
                return redirect(f"/edit_investor_poviat/{id}")
            elif (investor.investor_poviat != None and investor.investor_poviat.poviat_name != "nieokreślono") and (investor.investor_voivodeship == None or investor.investor_voivodeship.voivodeship_name == "nieokreślono"):
                investor.investor_poviat = None
                investor.save()
                return redirect("/investors")
            else:
                return redirect("/investors")


class EditInvestorPoviat(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        investor = Investor.objects.get(id=id)
        initial_data = {
            "investor_poviat": investor.investor_poviat
        }
        form = EditInvestorPoviatForm(initial=initial_data, investor=investor)
        ctx = {
            "investor": investor,
            "form": form,
            "divisions": divisions
        }
        return render(request, "edit_investor_poviat.html", ctx)

    def post(self, request, id):
        investor = Investor.objects.get(id=id)
        form = EditInvestorPoviatForm(request.POST, investor=investor)
        if form.is_valid():
            data = form.cleaned_data
            investor.investor_poviat = data["investor_poviat"]
            investor.save()
            return redirect(f"/investor_details/{id}")


class DeleteInvestor(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        investor = Investor.objects.get(id=id)
        ctx = {
            "investor": investor,
            "divisions": divisions
        }
        return render(request, "delete_investor.html", ctx)


class DeleteInvestorConfirm(View):
    def get(self, request, id):
        investor = Investor.objects.get(id=id)
        investor.delete()
        return redirect("/investors")


class AddCompany(View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = AddCompanyForm()
        ctx = {
            "form": form,
            "divisions": divisions
        }
        return render(request, "add_company.html", ctx)
    
    def post(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(id=request.session.get("division_id"))
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            company_name = data["company_name"]
            company_address = data["company_address"]
            company_voivodeship = data["company_voivodeship"]
            companies_names = [i.company_name for i in Company.objects.filter(division=division)]
            company = None
            if company_name not in companies_names:
                company = Company.objects.create(company_name=company_name, company_address=company_address,
                company_voivodeship=company_voivodeship, company_added_by=user)
            else:
                return redirect("/companies")
            company.division.add(division)
            company.save()
            if company.company_voivodeship != None and company.company_voivodeship.voivodeship_name != "nieokreślono":
                return redirect(f"/add_company_poviat/{company.id}")
            else:
                return redirect("/companies")


class AddCompanyPoviat(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        company = Company.objects.get(id=id)
        form = AddCompanyPoviatForm(company=company)
        ctx = {
            "form": form,
            "divisions": divisions,
            "company": company
        }
        return render(request, "add_company_poviat.html", ctx)
    
    def post(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        company = Company.objects.get(id=id)
        form = AddCompanyPoviatForm(request.POST, company=company)
        if form.is_valid():
            data = form.cleaned_data
            company_poviat = data["company_poviat"]
            company.company_poviat = company_poviat
            company.save()
            return redirect("/companies")


class CompaniesView(View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = None
        if request.session.get("division_id"):
            division = request.session["division_id"]
        form = SearchCompanyForm()
        companies = Company.objects.filter(division=division).order_by("company_name")

        paginator = Paginator(companies, 15)
        page = request.GET.get("page")
        companies = paginator.get_page(page)

        ctx = {
            "companies": companies,
            "divisions": divisions,
            "form": form
        }
        return render(request, "companies.html", ctx)
    
    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = SearchCompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            companies = Company.objects.filter(company_name__icontains=text).order_by("company_name")                           
            ctx = {
                "form": form,
                "companies": companies,
                "post": request.POST,
                "divisions": divisions
            }
            return render(request, "companies.html", ctx)


class CompanyDetails(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=request.session.get("division_id"))
        company = Company.objects.get(id=id)
        ctx = {
            "company": company,
            "divisions": divisions,
            "division": division
        }
        return render(request, "company_details.html", ctx)


class EditCompany(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        company = Company.objects.get(id=id)
        initial_data = {
            "company_name": company.company_name,
            "company_address": company.company_address,
            "company_voivodeship": company.company_voivodeship,
            "company_poviat": company.company_poviat
        }
        form = EditCompanyForm(initial=initial_data, company=company)
        ctx = {
            "company": company,
            "form": form,
            "divisions": divisions
        }
        return render(request, "edit_company.html", ctx)

    def post(self, request, id):
        company = Company.objects.get(id=id)
        form = EditCompanyForm(request.POST, company=company)
        if form.is_valid():
            data = form.cleaned_data
            company.company_name = data["company_name"]
            company.company_address = data["company_address"]
            company.company_voivodeship = data["company_voivodeship"]
            company.save()
            ctx = {
                "company": company
            }
            if company.company_voivodeship != None and company.company_voivodeship.voivodeship_name != "nieokreślono":
                return redirect(f"/edit_company_poviat/{id}")
            elif (company.company_poviat != None and company.company_poviat.poviat_name != "nieokreślono") and (company.company_voivodeship == None or company.company_voivodeship.voivodeship_name == "nieokreślono"):
                company.company_poviat = None
                company.save()
                return redirect("/companies")
            else:
                return redirect("/companies")


class EditCompanyPoviat(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        company = Company.objects.get(id=id)
        initial_data = {
            "company_poviat": company.company_poviat
        }
        form = EditCompanyPoviatForm(initial=initial_data, company=company)
        ctx = {
            "company": company,
            "form": form,
            "divisions": divisions
        }
        return render(request, "edit_company_poviat.html", ctx)

    def post(self, request, id):
        company = Company.objects.get(id=id)
        form = EditCompanyPoviatForm(request.POST, company=company)
        if form.is_valid():
            data = form.cleaned_data
            company.company_poviat = data["company_poviat"]
            company.save()
            ctx = {
                "company": company
            }
            return redirect(f"/company_details/{id}")


class DeleteCompany(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        company = Company.objects.get(id=id)
        ctx = {
            "company": company,
            "divisions": divisions
        }
        return render(request, "delete_company.html", ctx)


class DeleteCompanyConfirm(View):
    def get(self, request, id):
        company = Company.objects.get(id=id)
        company.delete()
        return redirect("/companies")


class AddDesigner(View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = AddDesignerForm()
        ctx = {
            "form": form,
            "divisions": divisions
        }
        return render(request, "add_designer.html", ctx)
    
    def post(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(id=request.session["division_id"])
        form = AddDesignerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            designer_name = data["designer_name"]
            designer_address = data["designer_address"]
            designer_voivodeship = data["designer_voivodeship"]
            designer_note = data["designer_note"]
            designers_names = [i.designer_name for i in Designer.objects.filter(division=division)]
            designer = None
            if designer_name not in designers_names:
                designer = Designer.objects.create(designer_name=designer_name, designer_address=designer_address,
                designer_voivodeship=designer_voivodeship, designer_added_by=user)
            else:
                return redirect("/designers")
            designer.division.add(division)
            noters = [i.designer_note_user for i in DesignerNote.objects.filter(designer_note_designer=designer)]
            if designer_note and not user in noters:
                new_designer_note = DesignerNote.objects.create(designer_note_designer=designer,
                designer_note_note=designer_note, designer_note_user=user)
                notes = [i.designer_note_note.note for i in DesignerNote.objects.filter(designer_note_designer=designer)]
                note_to_add = round(sum(notes)/len(notes), 2)
                designer.designer_note = note_to_add
            designer.save()
            if designer.designer_voivodeship != None and designer.designer_voivodeship.voivodeship_name != "nieokreślono":
                return redirect(f"/add_designer_poviat/{designer.id}")
            else:
                return redirect("/designers")


class AddDesignerPoviat(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        designer = Designer.objects.get(id=id)
        form = AddDesignerPoviatForm(designer=designer)
        ctx = {
            "form": form,
            "divisions": divisions,
            "designer": designer
        }
        return render(request, "add_designer_poviat.html", ctx)
    
    def post(self, request, id):
        designer = Designer.objects.get(id=id)
        form = AddDesignerPoviatForm(request.POST, designer=designer)
        if form.is_valid():
            data = form.cleaned_data
            designer_poviat = data["designer_poviat"]
            designer.designer_poviat = designer_poviat
            designer.save()
            return redirect("/designers")


class DesignersView(View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = None
        if request.session.get("division_id"):
            division = request.session["division_id"]
        form = SearchDesignerForm()
        designers = Designer.objects.filter(division=division).order_by("designer_name")

        paginator = Paginator(designers, 15)
        page = request.GET.get("page")
        designers = paginator.get_page(page)

        ctx = {
            "designers": designers,
            "divisions": divisions,
            "form": form
        }
        return render(request, "designers.html", ctx)
    
    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = SearchDesignerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            designers = Designer.objects.filter(designer_name__icontains=text).order_by("designer_name")                           
            ctx = {
                "form": form,
                "designers": designers,
                "post": request.POST,
                "divisions": divisions
            }
            return render(request, "designers.html", ctx)


class DesignerDetails(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=request.session.get("division_id"))
        designer = Designer.objects.get(id=id)
        noters = [i.designer_note_user for i in DesignerNote.objects.filter(designer_note_designer=designer)]
        form = DesignerNoteForm()
        ctx = {
            "designer": designer,
            "divisions": divisions,
            "division": division,
            "form": form,
            "noters": noters
        }
        return render(request, "designer_details.html", ctx)

    def post(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        form = DesignerNoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            designer = Designer.objects.get(id=id)
            designer_note = data["designer_note"]
            new_designer_note = DesignerNote.objects.create(designer_note_designer=designer,
            designer_note_note=designer_note, designer_note_user=user)
            notes = [i.designer_note_note.note for i in DesignerNote.objects.filter(designer_note_designer=designer)]
            note_to_add = round(sum(notes)/len(notes), 2)
            designer.designer_note = note_to_add
            designer.save()
            return redirect(f"/designer_details/{designer.id}")


class EditDesigner(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        designer = Designer.objects.get(id=id)
        initial_data = {
            "designer_name": designer.designer_name,
            "designer_address": designer.designer_address,
            "designer_voivodeship": designer.designer_voivodeship,
        }
        form = EditDesignerForm(initial=initial_data)
        ctx = {
            "designer": designer,
            "form": form,
            "divisions": divisions
        }
        return render(request, "edit_designer.html", ctx)

    def post(self, request, id):
        designer = Designer.objects.get(id=id)
        form = EditDesignerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            designer.designer_name = data["designer_name"]
            designer.designer_address = data["designer_address"]
            designer.designer_voivodeship = data["designer_voivodeship"]
            designer.save()
            ctx = {
                "designer": designer,
            }
            if designer.designer_voivodeship != None and designer.designer_voivodeship.voivodeship_name != "nieokreślono":
                return redirect(f"/edit_designer_poviat/{id}")
            elif (designer.designer_poviat != None and designer.designer_poviat.poviat_name != "nieokreślono") and (designer.designer_voivodeship == None or designer.designer_voivodeship.voivodeship_name == "nieokreślono"):
                designer.designer_poviat = None
                designer.save()
                return redirect("/designers")
            else:
                return redirect("/designers")


class EditDesignerPoviat(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        designer = Designer.objects.get(id=id)
        initial_data = {
            "designer_poviat": designer.designer_poviat
        }
        form = EditDesignerPoviatForm(initial=initial_data, designer=designer)
        ctx = {
            "designer": designer,
            "form": form,
            "divisions": divisions
        }
        return render(request, "edit_designer_poviat.html", ctx)

    def post(self, request, id):
        designer = Designer.objects.get(id=id)
        form = EditDesignerPoviatForm(request.POST, designer=designer)
        if form.is_valid():
            data = form.cleaned_data
            designer.designer_poviat = data["designer_poviat"]
            designer.save()
            return redirect(f"/designer_details/{id}")


class DeleteDesigner(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        designer = Designer.objects.get(id=id)
        ctx = {
            "designer": designer,
            "divisions": divisions
        }
        return render(request, "delete_designer.html", ctx)


class DeleteDesignerConfirm(View):
    def get(self, request, id):
        designer = Designer.objects.get(id=id)
        designer.delete()
        return redirect("/designers")


class DateChoiceView(View):
    def get(self, request):
        form = DateChoiceForm()
        return render(request, "date_choice.html")
    
    def post(self, request):
        pass

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
            if tender_time == "":
                tender_time = None
            open_time = data["open_time"]
            if open_time == "":
                open_time = None
            deposit = data["deposit"]
            announcement_number = data["announcement_number"]
            announcement_date = data["announcement_date"]
            if announcement_date == "":
                announcement_date = None
            voivodeship = data["voivodeship"]
            tender_date = data["tender_date"]
            if tender_date == "":
                tender_date = None
            project_name = data["project_name"]
            estimated_value = data["estimated_value"]            
            investor = data["investor"]
            project_deadline_date = data["project_deadline_date"]
            if project_deadline_date == "":
                project_deadline_date = None
            project_deadline_months = data["project_deadline_months"]
            project_deadline_days = data["project_deadline_days"]
            mma_quantity = data["mma_quantity"]
            payment_method = data["payment_method"]
            project_url = data["project_url"]
            if project_url == "":
                project_url = None
            person = data["person"]
            division = data["division"]
            rc_date = data["rc_date"]
            if rc_date == "":
                rc_date = None
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
                voivodeship=voivodeship, tender_date=tender_date, project_name=project_name,
                estimated_value=estimated_value, investor=investor, project_deadline_date=project_deadline_date,
                project_deadline_months=project_deadline_months, project_deadline_days=project_deadline_days,
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
            if project.voivodeship != None and project.voivodeship.voivodeship_name != "nieokreślono":
                return redirect(f"/add_project_poviat/{project.id}")
            else:
                return redirect("/projects")


class AddProjectPoviat(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        form = AddProjectPoviatForm(project=project)
        ctx = {
            "form": form,
            "project": project
        }
        return render(request, "add_project_poviat.html", ctx)
    
    def post(self, request, id):
        project = Project.objects.get(id=id)
        form = AddProjectPoviatForm(request.POST, project=project)
        if form.is_valid():
            data = form.cleaned_data
            poviat = data["poviat"]
            project.poviat = poviat
            project.save()
            return redirect("/projects")


class Projects(View):
    def get(self, request):
        user = None
        division = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        if request.session.get("division_id") not in ("", None):
            division = Division.objects.get(id=request.session.get("division_id"))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = SearchProjectForm()
        today = date.today()
        finish  = today + timedelta(days=100)
        projects1 = Project.objects.filter(division=division, tender_date__range=[today, finish], status=2).order_by("tender_date", "tender_time", "project_number")
        projects2 = Project.objects.filter(division=division, tender_date__isnull=True, status=2)
        projects = projects1 | projects2
        ctx = {
            "projects": projects,
            "divisions": divisions,
            "form": form
        }
        return render(request, "projects.html", ctx)
    
    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        today = date.today()
        finish = today + timedelta(days=100)
        form = SearchProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            projects1 = Project.objects.filter(project_name__icontains=text, tender_date__range=[today, finish], status=2).order_by("tender_date", "tender_time", "project_number")
            projects2 = Project.objects.filter(project_name__icontains=text, tender_date__isnull=True, status=2).order_by("tender_date", "tender_time", "project_number")
            projects = projects1 | projects2                            
            ctx = {
                "form": form,
                "projects": projects,
                "post": request.POST,
                "divisions": divisions
            }
            return render(request, "projects.html", ctx)


class ProjectDetails(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=id)
        ctx = {
            "project": project,
            "divisions": divisions
        }
        return render(request, "project_details.html", ctx)


class EditProject(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
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
            "project_deadline_date": project.project_deadline_date,
            "project_deadline_months": project.project_deadline_months,
            "project_deadline_days": project.project_deadline_days,
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
            "form": form,
            "divisions": divisions
        }
        return render(request, "edit_project.html", ctx)
    
    def post(self, request, id):
        form = EditProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.get(id=id)
            data = form.cleaned_data
            project.project_number = data["project_number"]
            if data["tender_time"] not in (None, ""):
                project.tender_time = data["tender_time"]
            if data["open_time"] not in (None, ""):
                project.open_time = data["open_time"]
            project.deposit = data["deposit"]
            project.announcement_number = data["announcement_number"]
            if data["announcement_date"] not in (None, ""):
                project.announcement_date = data["announcement_date"]
            project.voivodeship = data["voivodeship"]
            if data["tender_date"] not in (None, ""):
                project.tender_date = data["tender_date"]
            project_name = data["project_name"]
            project.estimated_value = data["estimated_value"]            
            project.investor = data["investor"]
            if data["project_deadline_date"] not in (None, ""):
                project.project_deadline_date = data["project_deadline_date"]
            project.project_deadline_months = data["project_deadline_months"]
            project.project_deadline_days = data["project_deadline_days"]
            project.mma_quantity = data["mma_quantity"]
            project.payment_method = data["payment_method"]
            if data["project_url"] not in (None, ""):
                project.project_url = data["project_url"]            
            project.person.set(data["person"])
            project.division = data["division"]
            if data["rc_date"] not in (None, ""):
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
            if project.voivodeship != None and project.voivodeship.voivodeship_name != "nieokreślono":
                return redirect(f"/edit_project_poviat/{id}")
            elif (project.poviat != None and project.poviat.poviat_name != "nieokreślono") and (project.voivodeship == None or project.voivodeship.voivodeship_name == "nieokreślono"):
                project.poviat = None
                project.save()
                return redirect("/projects")
            else:
                return redirect("/projects")


class EditProjectPoviat(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=id)
        initial_data = {
            "poviat": project.poviat
        }
        form = EditProjectPoviatForm(initial=initial_data, project=project)
        ctx = {
            "project": project,
            "form": form,
            "divisions": divisions
        }
        return render(request, "edit_project_poviat.html", ctx)
    
    def post(self, request, id):
        project = Project.objects.get(id=id)
        form = EditProjectPoviatForm(request.POST, project=project)
        if form.is_valid():
            data = form.cleaned_data
            project.poviat = data["poviat"]
            project.save()
            return redirect(f"/project_details/{id}")


class DeleteProject(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=id)
        ctx = {
            "project": project,
            "divisions": divisions
        }
        return render(request, "delete_project.html", ctx)
    

class DeleteProjectConfirm(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        if project.tender:
            project.tender.delete()
        project.delete()
        return redirect("/projects")


class ArchivesView(View):
    def get(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        if request.session.get("division_id") not in ("", None):
            division = Division.objects.get(id=request.session.get("division_id"))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = SearchArchiveForm()
        archives_date = date.today() + timedelta(days=-1)
        archives1 = Project.objects.filter(division=division, tender_date__range=["2021-01-01", archives_date])
        archives2 = Project.objects.filter(division=division).exclude(status=2)
        archives = archives1 | archives2
        archives = archives.order_by("-tender_date", "-tender_time", "-project_number")
        ctx = {
            "archives": archives,
            "divisions": divisions,
            "form": form
        }
        return render(request, "archives.html", ctx)
    
    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        today = date.today()
        finish = today + timedelta(days=100)
        form = SearchArchiveForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            archives_date = date.today() + timedelta(days=-1)
            archives1 = Project.objects.filter(project_name__icontains=text, tender_date__range=["2021-01-01", archives_date]).order_by("tender_date", "tender_time", "project_number")
            archives2 = Project.objects.filter(project_name__icontains=text).exclude(status=2).order_by("tender_date", "tender_time", "project_number")
            archives = archives1 | archives2              
            ctx = {
                "form": form,
                "archives": archives,
                "post": request.POST,
                "divisions": divisions
            }
            return render(request, "archives.html", ctx)


class AddDivisionView(View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = AddDivisionForm()
        ctx = {
            "form": form,
            "divisions": divisions
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
            return redirect("/division_choice")


class JoinDivisionView(View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = JoinDivisionForm()
        form.fields["division"].queryset = Division.objects.filter().exclude(division_person=user)
        ctx = {
            "form": form,
            "divisions": divisions
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
            return redirect("/division_choice")


class DivisionChoiceView(View):
    def get(self, request):
        user = None
        if request.session["user_id"] not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division_choice = Division.objects.filter(division_person=user)
        ctx = {
            "division_choice": division_choice,
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
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=id)
        ctx = {
            "division": division,
            "divisions": divisions
        }
        return render(request, "division_details.html", ctx)


class EditDivisionView(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=id)
        initial_data = {
            "division_name": division.division_name
        }
        form = EditDivisionForm(initial=initial_data)
        ctx = {
            "division": division,
            "form": form,
            "divisions": divisions
        }
        return render(request, "edit_division.html", ctx)

    def post(self, request, id):
        form = EditDivisionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            division = Division.objects.get(id=id)
            division.division_name = data["division_name"]
            division.save()
            ctx = {
                "division": division
            }
            return redirect(f"/division_details/{division.id}")


class DeleteDivisionView(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=id)
        ctx = {
            "division": division,
            "divisions": divisions
        }
        return render(request, "delete_division.html", ctx)


class DeleteDivisionConfirm(View):
    def get(self, request, id):
        division = Division.objects.get(id=id)
        division.delete()
        return redirect("/divisions")


class AddAdminView(View):
    def get(self, request, division_id, user_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(id=user_id)
        division.division_admin.add(user)
        division.save()
        user.is_staff = True
        user.save()
        return redirect(f"/division_details/{division.id}")


class CancelAdminView(View):
    def get(self, request, division_id, user_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(id=user_id)
        division.division_admin.remove(user)
        division.save()
        divisions = Division.objects.filter(division_admin=user)
        if len(divisions) == 0:
            user.is_staff = False
            user.save()
        return redirect(f"/division_details/{division.id}")


class AddPersonView(View):
    def get(self, request, division_id, user_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(id=user_id)
        division.division_person.add(user)
        division.division_wannabe.remove(user)
        division.save()
        return redirect(f"/division_details/{division.id}")


class RemoveMemberView(View):
    def get(self, request, division_id, user_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(id=user_id)
        division.division_person.remove(user)
        division.save()
        return redirect(f"/division_details/{division.id}")


class UserDetailsView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        ctx = {
            "user": user
        }
        return render(request, "user_details.html", ctx)


class AddTenderView(View):
    def get(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=id)
        form = AddTenderForm()
        ctx = {
            "project": project,
            "divisions": divisions,
            "form": form
        }
        return render(request, "add_tender.html", ctx)
    
    def post(self, request, id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=id)
        form = AddTenderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            budget = data["investor_budget"]
            value_weight = data["value_weight"]
            is_guarantee = data["is_guarantee"]
            is_deadline = data["is_deadline"]
            is_other_criteria = data["is_other_criteria"]
            tender = Tender.objects.create(investor_budget=budget, value_weight=value_weight, is_guarantee=is_guarantee,
                is_deadline=is_deadline, is_other_criteria=is_other_criteria)
            project.tender = tender
            project.save()
            return redirect(f"/add_tender_criteria/{project.id}/{tender.id}")


class AddTenderCriteria(View):
    def get(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        form = AddCriteriaForm(tender=tender)
        ctx = {
            "divisions": divisions,
            "project": project,
            "tender": tender,
            "form": form
        }
        return render(request, "add_tender_criteria.html", ctx)
    
    def post(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        form = AddCriteriaForm(request.POST, tender=tender)
        if form.is_valid():
            data = form.cleaned_data
            guarantee_min = None
            guarantee_max = None
            guarantee_weight = None
            guarantee = None
            if tender.is_guarantee:
                guarantee_min = data["guarantee_min"]
                guarantee_max = data["guarantee_max"]
                guarantee_weight = data["guarantee_weight"]
                guarantee = Guarantee.objects.create(weight=guarantee_weight, months_max=guarantee_max,
                months_min=guarantee_min)
                tender.guarantee = guarantee
                tender.save()
            deadline_min = None
            deadline_max = None
            deadline_weight = None
            deadline = None
            if tender.is_deadline:
                deadline_min = data["deadline_min"]
                deadline_max = data["deadline_max"]
                deadline_weight = data["deadline_weight"]
                deadline = Deadline.objects.create(weight=deadline_weight, months_min=deadline_min,
                months_max=deadline_max)
                tender.deadline = deadline
                tender.save()
            criteria = []
            if tender.is_other_criteria:
                criteria = data["criteria"]
                for i in criteria:
                    tender.other_criteria.add(i)
                    tender.save()
            return redirect(f"/add_other_criteria/{project.id}/{tender.id}")


class AddOtherCriteria(View):
    def get(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        count_value = int(tender.value_weight.weight)
        count_guarantee = 0
        if tender.guarantee:
            count_guarantee = int(tender.guarantee.weight.weight)
        count_deadline = 0
        if tender.deadline:
            count_deadline = int(tender.deadline.weight.weight)
        count = count_value + count_guarantee + count_deadline
        form = None
        if len(tender.other_criteria.all()) > 0:
            for i in tender.other_criteria.all():
                count += int(i.weight.weight)
        if tender.is_other_criteria:
            form = AddOtherCriteriaForm(count=count)
        ctx = {
            "divisions": divisions,
            "project": project,
            "tender": tender,
            "form": form,
            "count": count
        }
        return render(request, "add_other_criteria.html", ctx)
    
    def post(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        count_value = int(tender.value_weight.weight)
        count_guarantee = 0
        if tender.guarantee:
            count_guarantee = int(tender.guarantee.weight.weight)
        count_deadline = 0
        if tender.deadline:
            count_deadline = int(tender.deadline.weight.weight)
        count = count_value + count_guarantee + count_deadline
        form = None
        if len(tender.other_criteria.all()) > 0:
            for i in tender.other_criteria.all():
                count += int(i.weight.weight)
        form = AddOtherCriteriaForm(request.POST, count=count)
        if form.is_valid():
            data = form.cleaned_data
            criteria_name = data["criteria_name"]
            criteria_weight = data["criteria_weight"]
            for i in Criteria.objects.all():
                if criteria_name in (i.criteria_name, "termin", "Termin", "termin wykonania", "Termin wykonania",
                "gwarancja","Gwarancja", "Cena", "cena", "Wartość oferty",
                "wartość oferty") and criteria_weight.weight == i.weight.weight:
                    return redirect(f"/add_other_criteria/{project_id}/{tender_id}")
            for i in Criteria.objects.filter(tender=tender):
                if criteria_name in (i.criteria_name, "termin", "Termin", "termin wykonania", "Termin wykonania",
                "gwarancja","Gwarancja", "Cena", "cena", "Wartość oferty", "wartość oferty"):
                    return redirect(f"/add_other_criteria/{project_id}/{tender_id}")
            new_criteria = Criteria.objects.create(weight=criteria_weight, criteria_name=criteria_name)
            tender.other_criteria.add(new_criteria)
            tender.save()
            ctx = {
            "divisions": divisions,
            "project": project,
            "tender": tender,
            "form": form
            }
            return redirect(f"/add_other_criteria/{project_id}/{tender_id}")


class AddMissingCriteria(View):
    def post(self, request, project_id, tender_id, criteria_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        form_minor = AddMissingCriteriaForm(request.POST, tender=tender)
        if form_minor.is_valid():
            data = form_minor.cleaned_data
            criteria_value = data["criteria_value"]
            criteria = Criteria.objects.get(id=criteria_id)
            criteria.criteria_value = criteria_value
            criteria.save()
            return redirect(f"/add_tender_details/{project.id}/{tender.id}")


class AddTenderDetails(View):

    def get(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        form_major = AddTendererForm(tender=tender)
        form_minor = AddMissingCriteriaForm(tender=tender)
        ctx = {
            "divisions": divisions,
            "project": project,
            "tender": tender,
            "form_major": form_major,
            "form_minor": form_minor
        }
        return render(request, "add_tender_details.html", ctx)

    def post(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        form_major = AddTendererForm(request.POST, tender=tender)
        if form_major.is_valid():
            data = form_major.cleaned_data
            tenderer = data["tenderer"]
            offer_value = data["offer_value"]
            offer_guarantee = None
            if data.get("offer_guarantee") not in ("", None):
                offer_guarantee = data["offer_guarantee"]
            offer_deadline = None
            if data.get("offer_deadline", None) not in ("", None):
                offer_deadline = data.get("offer_deadline", None)
            tenderer = Tenderer.objects.create(tenderer=tenderer, offer_value=offer_value, offer_guarantee=offer_guarantee,
            offer_deadline=offer_deadline)
            for i in tender.other_criteria.all():
                criteria_value = data.get(f"criteria_value_{i.id}", None)
                criterium = Criteria.objects.create(criteria_name=i.criteria_name, weight=i.weight,
                criteria_value=criteria_value)
                tenderer.other_criteria.add(criterium)
            tenderer.save()                
            tender.tenderer.add(tenderer)
            tender.save()
            return redirect(f"/add_tender_details/{project.id}/{tender.id}")
    

class TenderDetailsView(View):

    def get(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        ctx = {
            "divisions": divisions,
            "project": project,
            "tender": tender
        }
        return render(request, "tender_details.html", ctx)


class EditTenderView(View):
    def get(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        initial_data = {
            "investor_budget": tender.investor_budget,
            "value_weight": tender.value_weight,
            "is_guarantee": tender.is_guarantee,
            "is_deadline": tender.is_deadline,
            "is_other_criteria": tender.is_other_criteria
        }
        form = EditTenderForm(initial=initial_data)
        ctx = {
            "project": project,
            "tender": tender,
            "divisions": divisions,
            "form": form
        }
        return render(request, "edit_tender.html", ctx)
    
    def post(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        form = EditTenderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tender.investor_budget = data["investor_budget"]
            tender.value_weight = data["value_weight"]
            tender.is_guarantee = data["is_guarantee"]
            if tender.is_guarantee == False:
                tender.guarantee = None
                tender.save()
            tender.is_deadline = data["is_deadline"]
            if tender.is_deadline == False:
                tender.deadline = None
                tender.save()
            tender.is_other_criteria = data["is_other_criteria"]
            if tender.is_other_criteria == False:
                tender.other_criteria.set([])
                tender.save()
            tender.save()
            return redirect(f"/edit_tender_criteria/{project.id}/{tender.id}")


class EditTenderCriteria(View):
    def get(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        initial_data = {
        }
        if tender.guarantee:
            initial_data["guarantee_min"] = tender.guarantee.months_min
            initial_data["guarantee_max"] = tender.guarantee.months_max
            initial_data["guarantee_weight"] = tender.guarantee.weight
        if tender.deadline:
            initial_data["deadline_min"] = tender.deadline.months_min
            initial_data["deadline_max"] = tender.deadline.months_max
            initial_data["deadline_weight"] = tender.deadline.weight
        if tender.other_criteria:
            initial_data["criteria"] = tender.other_criteria.all()
        form = EditCriteriaForm(initial=initial_data, tender=tender)
        ctx = {
            "divisions": divisions,
            "project": project,
            "tender": tender,
            "form": form
        }
        return render(request, "edit_tender_criteria.html", ctx)
    
    def post(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        form = EditCriteriaForm(request.POST, tender=tender)
        if form.is_valid():
            data = form.cleaned_data
            if tender.is_guarantee and tender.guarantee:
                tender.guarantee.months_min = data["guarantee_min"]
                tender.guarantee.months_max = data["guarantee_max"]
                tender.guarantee.weight = data["guarantee_weight"]
                tender.guarantee.save()
                tender.save()
            elif tender.is_guarantee and not tender.guarantee:
                guarantee_min = data["guarantee_min"]
                guarantee_max = data["guarantee_max"]
                guarantee_weight = data["guarantee_weight"]
                guarantee = Guarantee.objects.create(weight=guarantee_weight, months_max=guarantee_max,
                months_min=guarantee_min)
                tender.guarantee = guarantee
                tender.save()
            if tender.is_deadline and tender.deadline:
                tender.deadline.months_min = data["deadline_min"]
                tender.deadline.months_max = data["deadline_max"]
                tender.deadline.weight = data["deadline_weight"]
                tender.deadline.save()
                tender.save()
            elif tender.is_deadline and not tender.deadline:
                deadline_min = data["deadline_min"]
                deadline_max = data["deadline_max"]
                deadline_weight = data["deadline_weight"]
                deadline = Deadline.objects.create(weight=deadline_weight, months_min=deadline_min,
                months_max=deadline_max)
                tender.deadline = deadline
                tender.save()
            if tender.is_other_criteria:
                criteria = data["criteria"]
                tender.other_criteria.set(criteria)
                for i in tender.tenderer.all():
                    i.other_criteria.set([])
                    for j in criteria:
                        criterium = Criteria.objects.create(criteria_name=j.criteria_name, weight=j.weight)
                        i.other_criteria.add(criterium)
                        i.save()
                tender.save()
            return redirect(f"/add_other_criteria/{project.id}/{tender.id}")


class DeleteTendererView(View):
    def get(self, request, project_id, tender_id, tenderer_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        tenderer = Tenderer.objects.get(id=tenderer_id)
        tenderer.delete()
        return redirect(f"/add_tender_details/{project_id}/{tender_id}")


class DeleteOtherCriteriaView(View):
    def get(self, request, project_id, tender_id, criteria_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        criterium = Criteria.objects.get(id=criteria_id)
        criterium.delete()
        return redirect(f"/add_other_criteria/{project_id}/{tender_id}")


class DeleteTenderView(View):
    def get(self, request, project_id, tender_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        ctx = {
            "tender": tender,
            "project": project,
            "divisions": divisions
        }
        return render(request, "delete_tender.html", ctx)


class DeleteTenderConfirm(View):
    def get(self, request, project_id, tender_id):
        tender = Tender.objects.get(id=tender_id)
        tender.delete()
        return redirect("/projects")