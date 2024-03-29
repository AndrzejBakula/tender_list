from datetime import date, timedelta, timezone
from statistics import median

from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from horyzont_app.settings import PROTOCOLE

from django.db.models import Min

from .forms import (
    AddCompanyForm,
    AddCompanyPoviatForm,
    AddCriteriaForm,
    AddDesignerForm,
    AddDesignerPoviatForm,
    AddDivisionForm,
    AddInvestorForm,
    AddInvestorPoviatForm,
    AddMissingCriteriaForm,
    AddMissingDeadlineForm,
    AddMissingGuaranteeForm,
    AddOtherCriteriaForm,
    AddProjectForm,
    AddProjectPoviatForm,
    AddTendererForm,
    AddTenderForm,
    DesignerNoteForm,
    EditCompanyForm,
    EditCompanyPoviatForm,
    EditCriteriaForm,
    EditDesignerForm,
    EditDesignerPoviatForm,
    EditDivisionForm,
    EditInvestorForm,
    EditInvestorPoviatForm,
    EditOtherCriteriaForm,
    EditProjectForm,
    EditProjectPoviatForm,
    EditTenderForm,
    EditUserForm,
    InvestorNoteForm,
    JoinDivisionForm,
    LoginForm,
    RegisterForm,
    ResetForm,
    SearchArchiveForm,
    SearchCompanyForm,
    SearchDesignerForm,
    SearchInvestorForm,
    SearchProjectForm,
)
from .models import *
from .utils import token_generator


# INITIAL FUNCTIONS
# def values():
#     projects = Project.objects.all()
#     for i in projects:
#         if i.tender:
#             for j in i.tender.tenderer.all():
#                 if j.tenderer.company_name == "EUROVIA Polska S.A.":
#                     i.estimated_value = round(j.offer_value / 1.23, 2)
#                     i.save()


# values()


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
                if (0 < i[0] < 30) or i[0] == 380:
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


# AUXILIARY FUNCTIONS
def get_counter():
    counter = Counter.objects.all()[0]
    counter.counter += 1
    counter.save()
    return counter.counter


def validate_email(email):
    for i in User.objects.all():
        if i.email == email:
            return True
    return False


# USER CHECK CLASSES:
class VerificationView(View):
    def get(self, request, uidb64, token):
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        user.is_active = True
        user.save()
        return redirect("login")


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


class StaffMemberCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff


class ActivateUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_authenticated


# VIEW CLASSES
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
                "form": form,
            }
            return render(request, "register.html", ctx)
        elif len(password) < 8:
            message = "Hasło powinno mieć przynajmniej 8 znaków."
            ctx = {
                "username": username,
                "email": email,
                "message": message,
                "form": form,
            }
            return render(request, "register.html", ctx)
        elif username in ("", None) or email in ("", None) or password in ("", None):
            message = "Proszę wypełnić wszystkie pola."
            ctx = {
                "username": username,
                "email": email,
                "message": message,
                "form": form,
            }
            return render(request, "register.html", ctx)
        elif username in users:
            message = "Taki użytkownik jest już zarejestrowany."
            ctx = {"email": email, "message": message, "form": form}
            return render(request, "register.html", ctx)
        elif validate_email(email):
            message = "Ten email jest już zajęty."
            ctx = {"username": username, "message": message, "form": form}
            return render(request, "register.html", ctx)
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse(
                "activate",
                kwargs={"uidb64": uidb64, "token": token_generator.make_token(user)},
            )

            activate_url = PROTOCOLE + domain + link

            email_subject = "Aktywacja konta na Liście Przetargowej."
            email_body = (
                "Cześć "
                + user.username
                + "! Użyj, proszę, poniższego linku, żeby potwierdzić email.\n"
                + activate_url
            )
            email = EmailMessage(
                email_subject,
                email_body,
                "noreply@semycolon.com",
                [user.email],
            )
            email.send(fail_silently=False)

            message = f"Dodano nowego użytkownika {user.username}. Na podany email wysłano link aktywacyjny."
            form = LoginForm()
            ctx = {"message": message, "form": form}
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
        ctx = {"form": form, "message": message}
        return render(request, "login.html", ctx)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            request.session["logged"] = False
            user = request.user
            user.is_active = False
        return redirect("/projects")


class RequestPasswordResetEmail(View):
    def get(self, request):
        return render(request, "reset_password.html")

    def post(self, request):
        email = request.POST["email"]

        if not validate_email(email):
            message = "Podaj właściwy email."
            ctx = {"values": request.POST, "message": message}
            return render(request, "reset_password.html", ctx)

        current_site = get_current_site(request)
        user = User.objects.filter(email=email)
        if user.exists():
            email_contents = {
                "user": user[0],
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user[0].pk)),
                "token": PasswordResetTokenGenerator().make_token(user[0]),
            }
        link = reverse(
            "set-new-password",
            kwargs={"uidb64": email_contents["uid"], "token": email_contents["token"]},
        )
        email_subject = "Resetowanie hasła"
        reset_url = PROTOCOLE + current_site.domain + link
        email = EmailMessage(
            email_subject,
            "Cześć! By ustawić nowe hasło, kliknij proszę w poniższy link \n"
            + reset_url,
            "noreply@semycolon.com",
            [user[0].email],
        )
        email.send(fail_silently=False)
        message = "Wysłano link aktywacyjny na maila."
        ctx = {"message": message}
        return render(request, "reset_password.html", ctx)


class CompletePasswordReset(View):
    def get(self, request, uidb64, token):
        form = ResetForm()

        try:
            user_id = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                message = "Użyto niewłaściwego linku. Spróbuj z nowym."
                return render(request, "set_new_password.html", {"message": message})
        except Exception as identifier:
            pass

        ctx = {
            "uidb64": uidb64,
            "token": token,
            "form": form,
        }
        return render(request, "set_new_password.html", ctx)

    def post(self, request, uidb64, token):
        form = ResetForm(request.POST)
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            error_message = "Proszę podać dwa takie same hasła."
            ctx = {
                "uidb64": uidb64,
                "token": token,
                "error_message": error_message,
                "form": form,
            }
            return render(request, "set_new_password.html", ctx)
        elif len(password) < 8:
            error_message = "Hasło powinno mieć przynajmniej 8 znaków."
            ctx = {
                "uidb64": uidb64,
                "token": token,
                "error_message": error_message,
                "form": form,
            }
            return render(request, "set_new_password.html", ctx)
        try:
            user_id = urlsafe_base64_decode(uidb64)
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.save()
            message = "Hasło zostało ustawione."
            ctx = {"message": message}
            return render(request, "set_new_password.html", ctx)
        except Exception as identifier:
            message = "Coś poszło nie tak, spróbuj ponownie."
            ctx = {"message": message}
            return render(request, "set_new_password.html", ctx)


class AddInvestor(StaffMemberCheck, View):
    def get(self, request):
        counter = get_counter()
        if request.session.get("division_id"):  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            form = AddInvestorForm()
            ctx = {"form": form, "divisions": divisions}
            return render(request, "add_investor.html", ctx)
        return redirect("/projects")

    def post(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(id=request.session.get("division_id"))
        form = AddInvestorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            investor_name = data["investor_name"]
            investor_address = data["investor_address"]
            investor_email = data["investor_email"]
            investor_phone = data["investor_phone"]
            investor_voivodeship = data["investor_voivodeship"]
            investor_administration_level = data["investor_administration_level"]
            investor_note = data["investor_note"]
            investors_names = [
                i.investor_name for i in Investor.objects.filter(division=division)
            ]
            if not investor_name in investors_names:
                investor = Investor.objects.create(
                    investor_name=investor_name,
                    investor_address=investor_address,
                    investor_email=investor_email,
                    investor_phone=investor_phone,
                    investor_voivodeship=investor_voivodeship,
                    investor_administration_level=investor_administration_level,
                    investor_added_by=user,
                )
            else:
                return redirect("/investors")
            investor.division.add(division)
            noters = [
                i.investor_note_user
                for i in InvestorNote.objects.filter(investor_note_investor=investor)
            ]
            if investor_note and not user in noters:
                new_investor_note = InvestorNote.objects.create(
                    investor_note_investor=investor,
                    investor_note_note=investor_note,
                    investor_note_user=user,
                )
                notes = [
                    i.investor_note_note.note
                    for i in InvestorNote.objects.filter(
                        investor_note_investor=investor
                    )
                ]
                note_to_add = round(sum(notes) / len(notes), 2)
                investor.investor_note = note_to_add
            investor.save()
            if (
                investor.investor_voivodeship != None
                and investor.investor_voivodeship.voivodeship_name != "nieokreślono"
            ):
                return redirect(f"/add_investor_poviat/{investor.id}")
            else:
                return redirect("/investors")


class AddInvestorPoviat(StaffMemberCheck, View):
    def get(self, request, investor_id):
        investor = Investor.objects.get(id=investor_id)
        if request.session.get("division_id") in [
            i.id for i in investor.division.all()
        ]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            form = AddInvestorPoviatForm(investor=investor)
            ctx = {"form": form, "divisions": divisions, "investor": investor}
            return render(request, "add_investor_poviat.html", ctx)
        return redirect("/projects")

    def post(self, request, investor_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        investor = Investor.objects.get(id=investor_id)
        form = AddInvestorPoviatForm(request.POST, investor=investor)
        if form.is_valid():
            data = form.cleaned_data
            investor_poviat = data["investor_poviat"]
            investor.investor_poviat = investor_poviat
            investor.save()
            return redirect("/investors")


class InvestorsView(ActivateUserCheck, View):
    def get(self, request):
        counter = get_counter()
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=request.session.get("division_id"))
        investors = Investor.objects.filter(division=division).order_by("investor_name")
        all_investors = investors
        form = SearchInvestorForm()

        paginator = Paginator(investors, 15)
        page = request.GET.get("page")
        investors = paginator.get_page(page)

        ctx = {
            "investors": investors,
            "all_investors": all_investors,
            "divisions": divisions,
            "form": form,
        }
        return render(request, "investors.html", ctx)

    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=request.session.get("division_id"))
        form = SearchInvestorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            voivodeship = data["voivodeship"]
            poviat = data["poviat"]
            administration_level = data["administration_level"]
            investors = Investor.objects.filter(division=division).order_by(
                "investor_name"
            )
            investors1 = Investor.objects.filter(division=division).order_by(
                "investor_name"
            )
            if text:
                investors1 = Investor.objects.filter(
                    division=division, investor_name__icontains=text
                ).order_by("investor_name")
            investors2 = Investor.objects.filter(division=division).order_by(
                "investor_name"
            )
            if voivodeship:
                investors2 = Investor.objects.filter(
                    division=division, investor_voivodeship=voivodeship
                ).order_by("investor_name")
            investors3 = Investor.objects.filter(division=division).order_by(
                "investor_name"
            )
            if poviat:
                investors3 = Investor.objects.filter(
                    division=division, investor_poviat=poviat
                ).order_by("investor_name")
            investors4 = Investor.objects.filter(division=division).order_by(
                "investor_name"
            )
            if administration_level:
                investors4 = Investor.objects.filter(
                    division=division,
                    investor_administration_level=administration_level,
                ).order_by("investor_name")
            if text or voivodeship or poviat or administration_level:
                investors = investors1 & investors2 & investors3 & investors4

            # paginator = Paginator(investors, 15)
            # page = request.GET.get("page")
            # investors = paginator.get_page(page)

            ctx = {
                "form": form,
                "investors": investors,
                "post": request.POST,
                "divisions": divisions,
            }
            return render(request, "investors.html", ctx)


class InvestorDetails(ActivateUserCheck, View):
    def get(self, request, investor_id):
        investor = Investor.objects.get(id=investor_id)
        division = Division.objects.get(id=request.session.get("division_id"))
        if division in [i for i in investor.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            investor_projects = Project.objects.filter(
                investor=investor, division=division
            )
            active_projects = Project.objects.filter(
                investor=investor, division=division, status=2
            )
            won_projects = Project.objects.filter(
                investor=investor, division=division, status=5
            )
            annulled_projects = Project.objects.filter(
                investor=investor, division=division, status=4
            )
            abandoned_projects = Project.objects.filter(
                investor=investor, division=division, status=3
            )
            exclused_projects = Project.objects.filter(
                investor=investor, division=division, status=7
            )
            oldest_project = None
            if investor_projects.count() > 0:
                sorted_investor_projects = sorted(
                    investor_projects, key=lambda x: x.tender_date
                )
                oldest_project = sorted_investor_projects[0]
            noters = [
                i.investor_note_user
                for i in InvestorNote.objects.filter(investor_note_investor=investor)
            ]
            form = InvestorNoteForm()
            ctx = {
                "investor": investor,
                "divisions": divisions,
                "division": division,
                "investor_projects": investor_projects,
                "active_projects": active_projects,
                "won_projects": won_projects,
                "annulled_projects": annulled_projects,
                "abandoned_projects": abandoned_projects,
                "exclused_projects": exclused_projects,
                "oldest_project": oldest_project,
                "noters": noters,
                "form": form,
            }
            return render(request, "investor_details.html", ctx)
        return redirect("/projects")

    def post(self, request, investor_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        form = InvestorNoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            investor = Investor.objects.get(id=investor_id)
            investor_note = data["investor_note"]
            new_investor_note = InvestorNote.objects.create(
                investor_note_investor=investor,
                investor_note_note=investor_note,
                investor_note_user=user,
            )
            notes = [
                i.investor_note_note.note
                for i in InvestorNote.objects.filter(investor_note_investor=investor)
            ]
            note_to_add = round(sum(notes) / len(notes), 2)
            investor.investor_note = note_to_add
            investor.save()
            return redirect(f"/investor_details/{investor.id}")


class EditInvestor(StaffMemberCheck, View):
    def get(self, request, investor_id):
        investor = Investor.objects.get(id=investor_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division in [i for i in investor.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {
                "investor_name": investor.investor_name,
                "investor_address": investor.investor_address,
                "investor_email": investor.investor_email,
                "investor_phone": investor.investor_phone,
                "investor_voivodeship": investor.investor_voivodeship,
                "investor_administration_level": investor.investor_administration_level,
            }
            form = EditInvestorForm(initial=initial_data)
            ctx = {"investor": investor, "form": form, "divisions": divisions}
            return render(request, "edit_investor.html", ctx)
        return redirect("/projects")

    def post(self, request, investor_id):
        form = EditInvestorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            investor = Investor.objects.get(id=investor_id)
            investor.investor_name = data["investor_name"]
            investor.investor_address = data["investor_address"]
            investor.investor_email = data["investor_email"]
            investor.investor_phone = data["investor_phone"]
            investor.investor_voivodeship = data["investor_voivodeship"]
            investor.investor_administration_level = data[
                "investor_administration_level"
            ]
            investor.save()
            if (
                investor.investor_voivodeship != None
                and investor.investor_voivodeship.voivodeship_name != "nieokreślono"
            ):
                return redirect(f"/edit_investor_poviat/{investor_id}")
            elif (
                investor.investor_poviat != None
                and investor.investor_poviat.poviat_name != "nieokreślono"
            ) and (
                investor.investor_voivodeship == None
                or investor.investor_voivodeship.voivodeship_name == "nieokreślono"
            ):
                investor.investor_poviat = None
                investor.save()
                return redirect("/investors")
            else:
                return redirect("/investors")


class EditInvestorPoviat(StaffMemberCheck, View):
    def get(self, request, investor_id):
        investor = Investor.objects.get(id=investor_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division in [i for i in investor.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {"investor_poviat": investor.investor_poviat}
            form = EditInvestorPoviatForm(initial=initial_data, investor=investor)
            ctx = {"investor": investor, "form": form, "divisions": divisions}
            return render(request, "edit_investor_poviat.html", ctx)
        return redirect("/projects")

    def post(self, request, investor_id):
        investor = Investor.objects.get(id=investor_id)
        form = EditInvestorPoviatForm(request.POST, investor=investor)
        if form.is_valid():
            data = form.cleaned_data
            investor.investor_poviat = data["investor_poviat"]
            investor.save()
            return redirect(f"/investor_details/{investor_id}")


class DeleteInvestor(SuperUserCheck, View):
    def get(self, request, investor_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        investor = Investor.objects.get(id=investor_id)
        ctx = {"investor": investor, "divisions": divisions}
        return render(request, "delete_investor.html", ctx)


class DeleteInvestorConfirm(SuperUserCheck, View):
    def get(self, request, investor_id):
        investor = Investor.objects.get(id=investor_id)
        for i in InvestorNote.objects.filter(investor_note_investor=investor):
            i.delete()
        investor.delete()
        return redirect("/investors")


class AddCompany(StaffMemberCheck, View):
    def get(self, request):
        counter = get_counter()
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = AddCompanyForm()
        ctx = {"form": form, "divisions": divisions}
        return render(request, "add_company.html", ctx)

    def post(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(id=request.session.get("division_id"))
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            company_name = data["company_name"]
            company_address = data["company_address"]
            company_email = data["company_email"]
            company_phone = data["company_phone"]
            company_contact = data["company_contact"]
            is_subcontractor = data["is_subcontractor"]
            branch = data["branch"].title()
            company_voivodeship = data["company_voivodeship"]
            companies_names = [
                i.company_name for i in Company.objects.filter(division=division)
            ]
            company = None
            if company_name not in companies_names:
                company = Company.objects.create(
                    company_name=company_name,
                    company_address=company_address,
                    company_email=company_email,
                    company_phone=company_phone,
                    company_contact=company_contact,
                    is_subcontractor=is_subcontractor,
                    branch=branch,
                    company_voivodeship=company_voivodeship,
                    company_added_by=user,
                )
            else:
                return redirect("/companies")
            company.division.add(division)
            company.save()
            if (
                company.company_voivodeship != None
                and company.company_voivodeship.voivodeship_name != "nieokreślono"
            ):
                return redirect(f"/add_company_poviat/{company.id}")
            else:
                return redirect("/companies")


class AddCompanyPoviat(StaffMemberCheck, View):
    def get(self, request, company_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        company = Company.objects.get(id=company_id)
        form = AddCompanyPoviatForm(company=company)
        ctx = {"form": form, "divisions": divisions, "company": company}
        return render(request, "add_company_poviat.html", ctx)

    def post(self, request, company_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        company = Company.objects.get(id=company_id)
        form = AddCompanyPoviatForm(request.POST, company=company)
        if form.is_valid():
            data = form.cleaned_data
            company_poviat = data["company_poviat"]
            company.company_poviat = company_poviat
            company.save()
            return redirect("/companies")


class CompaniesView(ActivateUserCheck, View):
    def get(self, request):
        counter = get_counter()
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = None
        if request.session.get("division_id"):
            division = request.session["division_id"]
        form = SearchCompanyForm()
        companies = Company.objects.filter(division=division).order_by("company_name")
        division_company = None
        rest = None
        for i in companies:
            if i.division_company:
                division_company = i
                break
        if division_company:
            rest = (
                companies.filter()
                .exclude(id=division_company.id)
                .order_by("company_name")
            )
            companies = [division_company] + [i for i in rest]
        else:
            rest = companies.all().order_by("company_name")
            companies = [i for i in rest]
        all_companies = companies

        paginator = Paginator(companies, 15)
        page = request.GET.get("page")
        companies = paginator.get_page(page)

        ctx = {
            "companies": companies,
            "all_companies": all_companies,
            "divisions": divisions,
            "form": form,
            "division_company": division_company,
        }
        return render(request, "companies.html", ctx)

    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = None
        if request.session.get("division_id"):
            division = request.session["division_id"]
        form = SearchCompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            voivodeship = data["voivodeship"]
            poviat = data["poviat"]
            branch = data["branch"].title()
            is_subcontractor = data["is_subcontractor"]
            companies = Company.objects.filter(division=division).order_by(
                "company_name"
            )
            companies1 = Company.objects.filter(division=division).order_by(
                "company_name"
            )
            if text:
                companies1 = Company.objects.filter(
                    division=division, company_name__icontains=text
                ).order_by("company_name")
            companies2 = Company.objects.filter(division=division).order_by(
                "company_name"
            )
            if voivodeship:
                companies2 = Company.objects.filter(
                    division=division, company_voivodeship=voivodeship
                ).order_by("company_name")
            companies3 = Company.objects.filter(division=division).order_by(
                "company_name"
            )
            if poviat:
                companies3 = Company.objects.filter(
                    division=division, company_poviat=poviat
                ).order_by("company_name")
            companies4 = Company.objects.filter(division=division).order_by(
                "company_name"
            )
            if branch:
                companies4 = Company.objects.filter(
                    division=division, branch__icontains=branch
                )
            companies5 = Company.objects.filter(division=division).order_by(
                "company_name"
            )
            if is_subcontractor:
                companies5 = Company.objects.filter(
                    division=division, is_subcontractor=is_subcontractor
                )
            if text or voivodeship or poviat or branch or is_subcontractor:
                companies = (
                    companies1 & companies2 & companies3 & companies4 & companies5
                )
            division_company = None
            rest = None
            for i in companies:
                if i.division_company:
                    division_company = i
                    break
            if division_company:
                rest = (
                    companies.filter()
                    .exclude(id=division_company.id)
                    .order_by("company_name")
                )
                companies = [division_company] + [i for i in rest]
            else:
                rest = companies.all().order_by("company_name")
                companies = [i for i in rest]

            # paginator = Paginator(companies, 15)
            # page = request.GET.get("page")
            # companies = paginator.get_page(page)

            ctx = {
                "form": form,
                "companies": companies,
                "post": request.POST,
                "divisions": divisions,
                "division_company": division_company,
            }
            return render(request, "companies.html", ctx)


class AddMyCompanyView(StaffMemberCheck, View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        division = None
        if request.session.get("division_id"):
            division = Division.objects.get(id=request.session["division_id"])
        if (
            division in [i for i in company.division.all()]
            and len(division.division_company.all()) == 0
        ):  # url lock
            company.division_company = division
            company.save()
            return redirect("/companies")
        return redirect("/projects")


class RemoveMyCompanyView(StaffMemberCheck, View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        division = None
        if request.session.get("division_id"):
            division = Division.objects.get(id=request.session["division_id"])
        if (
            division in [i for i in company.division.all()] and company.division_company
        ):  # url lock
            company.division_company = None
            company.save()
            return redirect("/companies")
        return redirect("/projects")


class CompanyDetails(ActivateUserCheck, View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        division = Division.objects.get(id=request.session.get("division_id"))
        if division in [i for i in company.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            won_tenders = Tenderer.objects.filter(
                tenderer=company, tender__project__division=division, is_winner=True
            )
            oldest_project = None
            if company.tenderer_set.all().count() > 0:
                company_tenders = [
                    i.tender_set.all() for i in company.tenderer_set.all()
                ]
                company_projects = []
                for i in company_tenders:
                    if i.count() > 0:
                        company_projects.append(i[0].project)
                if len(company_projects) > 0:
                    company_projects = sorted(
                        company_projects, key=lambda x: x.tender_date
                    )
                if len(company_projects) > 0:
                    oldest_project = company_projects[0]
            ctx = {
                "company": company,
                "divisions": divisions,
                "division": division,
                "won_tenders": won_tenders,
                "oldest_project": oldest_project,
            }
            return render(request, "company_details.html", ctx)
        return redirect("/projects")


class EditCompany(StaffMemberCheck, View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        division = Division.objects.get(id=request.session.get("division_id"))
        if division in [i for i in company.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {
                "company_name": company.company_name,
                "company_address": company.company_address,
                "company_email": company.company_email,
                "company_phone": company.company_phone,
                "company_contact": company.company_contact,
                "is_subcontractor": company.is_subcontractor,
                "branch": company.branch,
                "company_voivodeship": company.company_voivodeship,
                "company_poviat": company.company_poviat,
            }
            form = EditCompanyForm(initial=initial_data, company=company)
            ctx = {"company": company, "form": form, "divisions": divisions}
            return render(request, "edit_company.html", ctx)
        return redirect("/projects")

    def post(self, request, company_id):
        company = Company.objects.get(id=company_id)
        form = EditCompanyForm(request.POST, company=company)
        if form.is_valid():
            data = form.cleaned_data
            company.company_name = data["company_name"]
            company.company_address = data["company_address"]
            company.company_email = data["company_email"]
            company.company_phone = data["company_phone"]
            company.company_contact = data["company_contact"]
            company.is_subcontractor = data["is_subcontractor"]
            company.branch = data["branch"].title()
            company.company_voivodeship = data["company_voivodeship"]
            company.save()
            ctx = {"company": company}
            if (
                company.company_voivodeship != None
                and company.company_voivodeship.voivodeship_name != "nieokreślono"
            ):
                return redirect(f"/edit_company_poviat/{company_id}")
            elif (
                company.company_poviat != None
                and company.company_poviat.poviat_name != "nieokreślono"
            ) and (
                company.company_voivodeship == None
                or company.company_voivodeship.voivodeship_name == "nieokreślono"
            ):
                company.company_poviat = None
                company.save()
                return redirect("/companies")
            else:
                return redirect("/companies")


class EditCompanyPoviat(StaffMemberCheck, View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        division = Division.objects.get(id=request.session.get("division_id"))
        if division in [i for i in company.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {"company_poviat": company.company_poviat}
            form = EditCompanyPoviatForm(initial=initial_data, company=company)
            ctx = {"company": company, "form": form, "divisions": divisions}
            return render(request, "edit_company_poviat.html", ctx)
        return redirect("/projects")

    def post(self, request, company_id):
        company = Company.objects.get(id=company_id)
        form = EditCompanyPoviatForm(request.POST, company=company)
        if form.is_valid():
            data = form.cleaned_data
            company.company_poviat = data["company_poviat"]
            company.save()
            ctx = {"company": company}
            return redirect(f"/company_details/{company_id}")


class DeleteCompany(SuperUserCheck, View):
    def get(self, request, company_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        company = Company.objects.get(id=company_id)
        ctx = {"company": company, "divisions": divisions}
        return render(request, "delete_company.html", ctx)


class DeleteCompanyConfirm(SuperUserCheck, View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        company.delete()
        return redirect("/companies")


class AddDesigner(StaffMemberCheck, View):
    def get(self, request):
        counter = get_counter()
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = AddDesignerForm()
        ctx = {"form": form, "divisions": divisions}
        return render(request, "add_designer.html", ctx)

    def post(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(id=request.session["division_id"])
        form = AddDesignerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            designer_name = data["designer_name"]
            designer_address = data["designer_address"]
            designer_email = data["designer_email"]
            designer_phone = data["designer_phone"]
            designer_voivodeship = data["designer_voivodeship"]
            designer_note = data["designer_note"]
            designers_names = [
                i.designer_name for i in Designer.objects.filter(division=division)
            ]
            designer = None
            if designer_name not in designers_names:
                designer = Designer.objects.create(
                    designer_name=designer_name,
                    designer_address=designer_address,
                    designer_email=designer_email,
                    designer_phone=designer_phone,
                    designer_voivodeship=designer_voivodeship,
                    designer_added_by=user,
                )
            else:
                return redirect("/designers")
            designer.division.add(division)
            noters = [
                i.designer_note_user
                for i in DesignerNote.objects.filter(designer_note_designer=designer)
            ]
            if designer_note and not user in noters:
                new_designer_note = DesignerNote.objects.create(
                    designer_note_designer=designer,
                    designer_note_note=designer_note,
                    designer_note_user=user,
                )
                notes = [
                    i.designer_note_note.note
                    for i in DesignerNote.objects.filter(
                        designer_note_designer=designer
                    )
                ]
                note_to_add = round(sum(notes) / len(notes), 2)
                designer.designer_note = note_to_add
            designer.save()
            if (
                designer.designer_voivodeship != None
                and designer.designer_voivodeship.voivodeship_name != "nieokreślono"
            ):
                return redirect(f"/add_designer_poviat/{designer.id}")
            else:
                return redirect("/designers")


class AddDesignerPoviat(StaffMemberCheck, View):
    def get(self, request, designer_id):
        designer = Designer.objects.get(id=designer_id)
        if request.session.get("division_id") in [
            i.id for i in designer.division.all()
        ]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            form = AddDesignerPoviatForm(designer=designer)
            ctx = {"form": form, "divisions": divisions, "designer": designer}
            return render(request, "add_designer_poviat.html", ctx)
        return redirect("/projects")

    def post(self, request, designer_id):
        designer = Designer.objects.get(id=designer_id)
        form = AddDesignerPoviatForm(request.POST, designer=designer)
        if form.is_valid():
            data = form.cleaned_data
            designer_poviat = data["designer_poviat"]
            designer.designer_poviat = designer_poviat
            designer.save()
            return redirect("/designers")


class DesignersView(ActivateUserCheck, View):
    def get(self, request):
        counter = get_counter()
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = None
        if request.session.get("division_id"):
            division = Division.objects.get(pk=request.session["division_id"])
        form = SearchDesignerForm()
        designers = Designer.objects.filter(division=division).order_by("designer_name")
        all_designers = designers

        paginator = Paginator(designers, 15)
        page = request.GET.get("page")
        designers = paginator.get_page(page)

        ctx = {
            "designers": designers,
            "all_designers": all_designers,
            "divisions": divisions,
            "form": form,
        }
        return render(request, "designers.html", ctx)

    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(pk=request.session["division_id"])
        form = SearchDesignerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            voivodeship = data["voivodeship"]
            poviat = data["poviat"]
            designers = Designer.objects.filter(division=division).order_by(
                "designer_name"
            )
            designers1 = Designer.objects.filter(division=division).order_by(
                "designer_name"
            )
            if text:
                designers1 = Designer.objects.filter(
                    division=division, designer_name__icontains=text
                ).order_by("designer_name")
            designers2 = Designer.objects.filter(division=division).order_by(
                "designer_name"
            )
            if voivodeship:
                designers2 = Designer.objects.filter(
                    division=division, designer_voivodeship=voivodeship
                ).order_by("designer_name")
            designers3 = Designer.objects.filter(division=division).order_by(
                "designer_name"
            )
            if poviat:
                designers3 = Designer.objects.filter(
                    division=division, designer_poviat=poviat
                ).order_by("designer_name")
            if text or voivodeship or poviat:
                designers = designers1 & designers2 & designers3

            # paginator = Paginator(designers, 15)
            # page = request.GET.get("page")
            # designers = paginator.get_page(page)

            ctx = {
                "form": form,
                "designers": designers,
                "post": request.POST,
                "divisions": divisions,
            }
            return render(request, "designers.html", ctx)


class DesignerDetails(ActivateUserCheck, View):
    def get(self, request, designer_id):
        designer = Designer.objects.get(id=designer_id)
        division = Division.objects.get(id=request.session.get("division_id"))
        if division in [i for i in designer.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            division_designer = Project.objects.filter(
                designer=designer, division=division
            )
            oldest_project = None
            if division_designer.count() > 0:
                sorted_division_designer = sorted(
                    division_designer, key=lambda x: x.tender_date
                )
                oldest_project = sorted_division_designer[0]
            noters = [
                i.designer_note_user
                for i in DesignerNote.objects.filter(designer_note_designer=designer)
            ]
            form = DesignerNoteForm()
            ctx = {
                "designer": designer,
                "divisions": divisions,
                "division": division,
                "division_designer": division_designer,
                "form": form,
                "oldest_project": oldest_project,
                "noters": noters,
            }
            return render(request, "designer_details.html", ctx)
        return redirect("/projects")

    def post(self, request, designer_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        form = DesignerNoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            designer = Designer.objects.get(id=designer_id)
            designer_note = data["designer_note"]
            new_designer_note = DesignerNote.objects.create(
                designer_note_designer=designer,
                designer_note_note=designer_note,
                designer_note_user=user,
            )
            notes = [
                i.designer_note_note.note
                for i in DesignerNote.objects.filter(designer_note_designer=designer)
            ]
            note_to_add = round(sum(notes) / len(notes), 2)
            designer.designer_note = note_to_add
            designer.save()
            return redirect(f"/designer_details/{designer.id}")


class EditDesigner(StaffMemberCheck, View):
    def get(self, request, designer_id):
        designer = Designer.objects.get(id=designer_id)
        division = Division.objects.get(id=request.session.get("division_id"))
        if division in [i for i in designer.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {
                "designer_name": designer.designer_name,
                "designer_address": designer.designer_address,
                "designer_email": designer.designer_email,
                "designer_phone": designer.designer_phone,
                "designer_email": designer.designer_email,
                "designer_voivodeship": designer.designer_voivodeship,
            }
            form = EditDesignerForm(initial=initial_data)
            ctx = {"designer": designer, "form": form, "divisions": divisions}
            return render(request, "edit_designer.html", ctx)
        return redirect("/projects")

    def post(self, request, designer_id):
        designer = Designer.objects.get(id=designer_id)
        form = EditDesignerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            designer.designer_name = data["designer_name"]
            designer.designer_address = data["designer_address"]
            designer.designer_email = data["designer_email"]
            designer.designer_phone = data["designer_phone"]
            designer.designer_email = data["designer_email"]
            designer.designer_voivodeship = data["designer_voivodeship"]
            designer.save()
            ctx = {
                "designer": designer,
            }
            if (
                designer.designer_voivodeship != None
                and designer.designer_voivodeship.voivodeship_name != "nieokreślono"
            ):
                return redirect(f"/edit_designer_poviat/{designer_id}")
            elif (
                designer.designer_poviat != None
                and designer.designer_poviat.poviat_name != "nieokreślono"
            ) and (
                designer.designer_voivodeship == None
                or designer.designer_voivodeship.voivodeship_name == "nieokreślono"
            ):
                designer.designer_poviat = None
                designer.save()
                return redirect("/designers")
            else:
                return redirect("/designers")


class EditDesignerPoviat(StaffMemberCheck, View):
    def get(self, request, designer_id):
        designer = Designer.objects.get(id=designer_id)
        division = Division.objects.get(id=request.session.get("division_id"))
        if division in [i for i in designer.division.all()]:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {"designer_poviat": designer.designer_poviat}
            form = EditDesignerPoviatForm(initial=initial_data, designer=designer)
            ctx = {"designer": designer, "form": form, "divisions": divisions}
            return render(request, "edit_designer_poviat.html", ctx)
        return redirect("/projects")

    def post(self, request, designer_id):
        designer = Designer.objects.get(id=designer_id)
        form = EditDesignerPoviatForm(request.POST, designer=designer)
        if form.is_valid():
            data = form.cleaned_data
            designer.designer_poviat = data["designer_poviat"]
            designer.save()
            return redirect(f"/designer_details/{designer_id}")


class DeleteDesigner(SuperUserCheck, View):
    def get(self, request, designer_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        designer = Designer.objects.get(id=designer_id)
        ctx = {"designer": designer, "divisions": divisions}
        return render(request, "delete_designer.html", ctx)


class DeleteDesignerConfirm(SuperUserCheck, View):
    def get(self, request, designer_id):
        designer = Designer.objects.get(id=designer_id)
        for i in DesignerNote.objects.filter(designer_note_designer=designer):
            i.delte()
        designer.delete()
        return redirect("/designers")


class AddProject(StaffMemberCheck, View):
    def get(self, request):
        counter = get_counter()
        user = None
        division = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        if request.session.get("division_id") not in ("", None):
            division = Division.objects.get(id=request.session.get("division_id"))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = AddProjectForm(user=user, division=division)
        ctx = {"form": form, "division": division, "divisions": divisions}
        return render(request, "add_project.html", ctx)

    def post(self, request):
        user = None
        division = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        if request.session.get("division_id") not in ("", None):
            division = Division.objects.get(id=request.session.get("division_id"))
        form = AddProjectForm(request.POST, user=user, division=division)
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
                project_number=project_number,
                tender_time=tender_time,
                open_time=open_time,
                deposit=deposit,
                announcement_number=announcement_number,
                announcement_date=announcement_date,
                voivodeship=voivodeship,
                tender_date=tender_date,
                project_name=project_name,
                estimated_value=estimated_value,
                investor=investor,
                project_deadline_date=project_deadline_date,
                project_deadline_months=project_deadline_months,
                project_deadline_days=project_deadline_days,
                mma_quantity=mma_quantity,
                payment_method=payment_method,
                project_url=project_url,
                division=division,
                rc_date=rc_date,
                rc_agree=rc_agree,
                evaluation_criteria=evaluation_criteria,
                payment_criteria=payment_criteria,
                remarks=remarks,
                priority=priority,
                designer=designer,
                status=status,
            )
            for i in person:
                project.person.add(i)
            for i in jv_partners:
                project.jv_partners.add(i)
            project.save()
            if (
                project.voivodeship != None
                and project.voivodeship.voivodeship_name != "nieokreślono"
            ):
                return redirect(f"/add_project_poviat/{project.id}")
            else:
                return redirect("/projects")
        error_message = "Sprawdź komunikaty walidacyjne i spróbój ponownie"
        ctx = {
            "form": form,
            "division": division,
            "divisions": divisions,
            "error_message": error_message,
        }
        return render(request, "add_project.html", ctx)


class AddProjectPoviat(StaffMemberCheck, View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        division = None
        if request.session.get("division_id"):
            division = Division.objects.get(id=request.session.get("division_id"))
        if division == project.division:  # url lock
            user = None
            if request.session.get("user_id") not in ("", None):
                user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            form = AddProjectPoviatForm(project=project)
            ctx = {"form": form, "project": project}
            return render(request, "add_project_poviat.html", ctx)
        return redirect("/projects")

    def post(self, request, project_id):
        project = Project.objects.get(id=project_id)
        form = AddProjectPoviatForm(request.POST, project=project)
        if form.is_valid():
            data = form.cleaned_data
            poviat = data["poviat"]
            project.poviat = poviat
            project.save()
            return redirect("/projects")


class Projects(View):
    def get(self, request):
        counter = get_counter()
        user = None
        division = None
        if request.session.get("user_id"):
            user = User.objects.get(pk=int(request.session["user_id"]))
        if request.session.get("division_id"):
            division = Division.objects.get(id=request.session.get("division_id"))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = SearchProjectForm()
        today = date.today()
        finish = today + timedelta(days=100)
        projects1 = Project.objects.filter(
            division=division, tender_date__range=[today, finish], status=2
        ).order_by("tender_date", "tender_time", "project_number")
        projects2 = Project.objects.filter(
            division=division, tender_date__isnull=True, status=2
        ).order_by("tender_date", "tender_time", "project_number")
        projects = projects1 | projects2
        users = User.objects.filter(is_active=True)

        paginator = Paginator(projects, 15)
        page = request.GET.get("page")
        projects = paginator.get_page(page)

        ctx = {
            "projects": projects,
            "divisions": divisions,
            "form": form,
            "counter": counter,
            "users": users,
        }
        return render(request, "projects.html", ctx)

    def post(self, request):
        user = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = Division.objects.get(id=request.session.get("division_id"))
        today = date.today()
        finish = today + timedelta(days=100)
        form = SearchProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            projects1 = Project.objects.filter(
                division=division,
                project_name__icontains=text,
                tender_date__range=[today, finish],
                status=2,
            ).order_by("tender_date", "tender_time", "project_number")
            projects2 = Project.objects.filter(
                division=division,
                project_name__icontains=text,
                tender_date__isnull=True,
                status=2,
            ).order_by("tender_date", "tender_time", "project_number")
            projects = projects1 | projects2
            ctx = {
                "form": form,
                "projects": projects,
                "post": request.POST,
                "divisions": divisions,
            }
            return render(request, "projects.html", ctx)


class ProjectDetails(ActivateUserCheck, View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            ctx = {"project": project, "divisions": divisions}
            return render(request, "project_details.html", ctx)
        return redirect("/projects")


class EditProject(StaffMemberCheck, View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        division = None
        if request.session.get("division_id"):
            division = Division.objects.get(id=request.session.get("division_id"))
        if division == project.division:  # url lock
            user = None
            if request.session.get("user_id"):
                user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
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
                "rc_date": project.rc_date,
                "rc_agree": project.rc_agree,
                "evaluation_criteria": project.evaluation_criteria,
                "payment_criteria": project.payment_criteria,
                "jv_partners": [i for i in project.jv_partners.all()],
                "remarks": project.remarks,
                "priority": project.priority,
                "designer": project.designer,
                "status": project.status,
            }
            form = EditProjectForm(initial=initial_data, user=user, division=division)
            ctx = {"project": project, "form": form, "divisions": divisions}
            return render(request, "edit_project.html", ctx)
        return redirect("/projects")

    def post(self, request, project_id):
        project = Project.objects.get(id=project_id)
        user = None
        division = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        if request.session.get("division_id") not in ("", None):
            division = Division.objects.get(id=request.session.get("division_id"))
        form = EditProjectForm(request.POST, user=user, division=division)
        if form.is_valid():
            project = Project.objects.get(id=project_id)
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
            project.project_name = data["project_name"]
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
            project.division = division
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
            if (
                project.voivodeship != None
                and project.voivodeship.voivodeship_name != "nieokreślono"
            ):
                return redirect(f"/edit_project_poviat/{project_id}")
            elif (
                project.poviat != None and project.poviat.poviat_name != "nieokreślono"
            ) and (
                project.voivodeship == None
                or project.voivodeship.voivodeship_name == "nieokreślono"
            ):
                project.poviat = None
                project.save()
                return redirect("/projects")
            else:
                return redirect("/projects")
        error_message = "Sprawdź komunikaty walidacyjne i spróbój ponownie"
        ctx = {
            "form": form,
            "division": division,
            "divisions": divisions,
            "error_message": error_message,
            "project": project,
        }
        return render(request, "edit_project.html", ctx)


class EditProjectPoviat(StaffMemberCheck, View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {"poviat": project.poviat}
            form = EditProjectPoviatForm(initial=initial_data, project=project)
            ctx = {"project": project, "form": form, "divisions": divisions}
            return render(request, "edit_project_poviat.html", ctx)
        return redirect("/projects")

    def post(self, request, project_id):
        project = Project.objects.get(id=project_id)
        form = EditProjectPoviatForm(request.POST, project=project)
        if form.is_valid():
            data = form.cleaned_data
            project.poviat = data["poviat"]
            project.save()
            return redirect(f"/project_details/{project_id}")


class DeleteProject(StaffMemberCheck, View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            ctx = {"project": project, "divisions": divisions}
            return render(request, "delete_project.html", ctx)
        return redirect("/projects")


class DeleteProjectConfirm(StaffMemberCheck, View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division:  # url lock
            if project.tender:
                tender = project.tender
                tenderers = Tenderer.objects.filter(tender=tender)
                for i in tenderers:
                    criteria = Criteria.objects.filter(tenderer=i)
                    for j in criteria:
                        j.delete()
                    i.delete()
                criteria = Criteria.objects.filter(tender=tender)
                for i in criteria:
                    i.delete()
                tender.delete()
            project.delete()
        return redirect("/projects")


class ArchivesView(ActivateUserCheck, View):
    def get(self, request):
        counter = get_counter()
        user = None
        division = None
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        if request.session.get("division_id") not in ("", None):
            division = Division.objects.get(id=request.session.get("division_id"))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        form = SearchArchiveForm(division=division)
        archives_date = date.today() + timedelta(days=-1)
        archives1 = Project.objects.filter(
            division=division, tender_date__range=["2021-01-01", archives_date]
        ).order_by("-tender_date", "-tender_time", "-project_number")
        archives2 = (
            Project.objects.filter(division=division)
            .exclude(status=2)
            .order_by("-tender_date", "-tender_time", "-project_number")
        )
        archives = archives1 | archives2
        archives_all = archives
        oldest_project = None
        if archives.count() > 0:
            oldest_project = archives.reverse()[0]
        mma_list = []
        if archives.count() > 0:
            mma_list = [i.mma_quantity for i in archives]
        for i in range(len(mma_list)):
            if mma_list[i] == None:
                mma_list[i] = 0
        mma_sum = round(sum(mma_list), 2)
        mma_avarange = 0
        if archives.count() > 0:
            mma_avarange = round(mma_sum / archives.count(), 2)
        mma_median = 0
        if archives.count() > 0:
            mma_median = round(median(mma_list), 2)
        deposit_list = []
        if archives.count() > 0:
            deposit_list = [i.deposit for i in archives]
        for i in range(len(deposit_list)):
            if deposit_list[i] == None:
                deposit_list[i] = 0
        deposit_sum = round(sum(deposit_list), 2)
        deposit_avarange = 0
        if archives.count() > 0:
            deposit_avarange = round(deposit_sum / archives.count(), 2)
        deposit_median = 0
        if archives.count() > 0:
            deposit_median = round(median(deposit_list), 2)
        value_sum = round(
            sum([i.estimated_value for i in archives if i.estimated_value != None]), 2
        )
        value_avarange = 0
        if archives.count() > 0:
            value_avarange = round(value_sum / archives.count(), 2)
        value_median = 0
        if archives.count() > 0:
            value_median = round(
                median(
                    [i.estimated_value for i in archives if i.estimated_value != None]
                ),
                2,
            )
        tenders = archives.exclude(status=1).exclude(status=2).exclude(status=3)
        investor_list = []
        if archives.count() > 0:
            investor_list = [i.investor.investor_name for i in archives]
        super_investor = max(investor_list, key=investor_list.count)
        payment_method_list = []
        if archives.count() > 0:
            payment_method_list = [
                i.payment_method.payment_method_name
                for i in archives
                if i.payment_method != None
            ]
        super_payment_method = max(payment_method_list, key=payment_method_list.count)
        person_list = []
        if archives.count() > 0:
            person_sets = [i.person.all() for i in archives if i.person.all() != None]
            for i in person_sets:
                for j in i:
                    person_list.append(j.username)
        super_person = None
        if len(person_list) > 0:
            super_person = max(person_list, key=person_list.count)

        paginator = Paginator(archives, 15)
        page = request.GET.get("page")
        archives = paginator.get_page(page)

        ctx = {
            "archives": archives,
            "archives_all": archives_all,
            "divisions": divisions,
            "form": form,
            "oldest_project": oldest_project,
            "mma_sum": mma_sum,
            "mma_avarange": mma_avarange,
            "mma_median": mma_median,
            "deposit_sum": deposit_sum,
            "deposit_avarange": deposit_avarange,
            "deposit_median": deposit_median,
            "value_sum": value_sum,
            "value_avarange": value_avarange,
            "value_median": value_median,
            "tenders": tenders,
            "super_investor": super_investor,
            "super_payment_method": super_payment_method,
            "super_person": super_person,
        }
        return render(request, "archives.html", ctx)

    def post(self, request):
        user = None
        division = Division.objects.get(id=request.session.get("division_id"))
        if request.session.get("user_id") not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        today = date.today()
        finish = today + timedelta(days=100)
        form = SearchArchiveForm(request.POST, division=division)
        if form.is_valid():
            data = form.cleaned_data
            text = data["text"]
            investor = data["investor"]
            designer = data["designer"]
            payment_method = data["payment_method"]
            person = data["person"]
            status = data["status"]
            date_start = data["date_start"]
            date_end = data["date_end"]
            archives1 = (
                Project.objects.filter(division=division)
                .exclude(status=2)
                .order_by("-tender_date", "-tender_time", "-project_number")
            )
            if text:
                archives1 = (
                    Project.objects.filter(
                        project_name__icontains=text,
                        division=division,
                    )
                    .exclude(status=2)
                    .order_by("-tender_date", "-tender_time", "-project_number")
                )
            archives2 = (
                Project.objects.filter(division=division)
                .exclude(status=2)
                .order_by("-tender_date", "-tender_time", "-project_number")
            )
            if investor:
                archives2 = (
                    Project.objects.filter(
                        investor=investor,
                        division=division,
                    )
                    .exclude(status=2)
                    .order_by("-tender_date", "-tender_time", "-project_number")
                )
            archives8 = (
                Project.objects.filter(division=division)
                .exclude(status=2)
                .order_by("-tender_date", "-tender_time", "-project_number")
            )
            if designer:
                archives8 = (
                    Project.objects.filter(
                        designer=designer,
                        division=division,
                    )
                    .exclude(status=2)
                    .order_by("-tender_date", "-tender_time", "-project_number")
                )
            archives3 = (
                Project.objects.filter(division=division)
                .exclude(status=2)
                .order_by("-tender_date", "-tender_time", "-project_number")
            )
            if payment_method:
                archives3 = (
                    Project.objects.filter(
                        payment_method=payment_method,
                        division=division,
                    )
                    .exclude(status=2)
                    .order_by("-tender_date", "-tender_time", "-project_number")
                )
            archives4 = (
                Project.objects.filter(division=division)
                .exclude(status=2)
                .order_by("-tender_date", "-tender_time", "-project_number")
            )
            if person:
                archives4 = (
                    Project.objects.filter(
                        person=person,
                        division=division,
                    )
                    .exclude(status=2)
                    .order_by("-tender_date", "-tender_time", "-project_number")
                )
            archives5 = (
                Project.objects.filter(division=division)
                .exclude(status=2)
                .order_by("-tender_date", "-tender_time", "-project_number")
            )
            if status:
                archives5 = (
                    Project.objects.filter(
                        status__in=status,
                        division=division,
                    )
                    .exclude(status=2)
                    .order_by("-tender_date", "-tender_time", "-project_number")
                )
            archives6 = (
                Project.objects.filter(division=division)
                .exclude(status=2)
                .order_by("-tender_date", "-tender_time", "-project_number")
            )
            if date_start:
                archives6 = (
                    Project.objects.filter(
                        tender_date__gte=date_start,
                        division=division,
                    )
                    .exclude(status=2)
                    .order_by("-tender_date", "-tender_time", "-project_number")
                )
            archives7 = (
                Project.objects.filter(division=division)
                .exclude(status=2)
                .order_by("-tender_date", "-tender_time", "-project_number")
            )
            if date_end:
                archives7 = (
                    Project.objects.filter(
                        tender_date__lte=date_end,
                        division=division,
                    )
                    .exclude(status=2)
                    .order_by("-tender_date", "-tender_time", "-project_number")
                )
            archives = (
                archives1
                & archives2
                & archives3
                & archives4
                & archives5
                & archives6
                & archives7
                & archives8
            )
            archives_all = archives
            oldest_project = None
            if archives.count() > 0:
                oldest_project = archives.reverse()[0]
            mma_list = []
            if archives.count() > 0:
                mma_list = [i.mma_quantity for i in archives]
            for i in range(len(mma_list)):
                if mma_list[i] == None:
                    mma_list[i] = 0
            mma_sum = round(sum(mma_list), 2)
            mma_avarange = 0
            if archives.count() > 0:
                mma_avarange = round(mma_sum / archives.count(), 2)
            mma_median = 0
            if archives.count() > 0:
                mma_median = round(median(mma_list), 2)
            deposit_list = []
            if archives.count() > 0:
                deposit_list = [i.deposit for i in archives]
            for i in range(len(deposit_list)):
                if deposit_list[i] == None:
                    deposit_list[i] = 0
            deposit_sum = round(sum(deposit_list), 2)
            deposit_avarange = 0
            if archives.count() > 0:
                deposit_avarange = round(deposit_sum / archives.count(), 2)
            deposit_median = 0
            if archives.count() > 0:
                deposit_median = round(median(deposit_list), 2)
            value_list = []
            if archives.count() > 0:
                value_list = [
                    i.estimated_value for i in archives if i.estimated_value != None
                ]
            value_sum = round(sum(value_list), 2)
            value_avarange = 0
            if archives.count() > 0:
                value_avarange = round(value_sum / archives.count(), 2)
            value_median = 0
            if archives.count() > 0 and len(value_list) > 0:
                value_median = round(median(value_list), 2)
            tenders = archives.exclude(status=1).exclude(status=2).exclude(status=3)
            investor_list = []
            if archives.count() > 0:
                investor_list = [i.investor.investor_name for i in archives]
            super_investor = None
            if len(investor_list) > 0:
                super_investor = max(investor_list, key=investor_list.count)
            payment_method_list = []
            if archives.count() > 0:
                payment_method_list = [
                    i.payment_method.payment_method_name
                    for i in archives
                    if i.payment_method != None
                ]
            super_payment_method = None
            if len(payment_method_list) > 0:
                super_payment_method = max(
                    payment_method_list, key=payment_method_list.count
                )
            person_list = []
            if archives.count() > 0:
                person_sets = [
                    i.person.all() for i in archives if i.person.all() != None
                ]
                for i in person_sets:
                    for j in i:
                        person_list.append(j.username)
            super_person = None
            if len(person_list) > 0:
                super_person = max(person_list, key=person_list.count)

            # paginator = Paginator(archives, 15)
            # page = request.GET.get("page")
            # archives = paginator.get_page(page)

            ctx = {
                "form": form,
                "archives": archives,
                "archives_all": archives_all,
                "divisions": divisions,
                "oldest_project": oldest_project,
                "mma_sum": mma_sum,
                "mma_avarange": mma_avarange,
                "mma_median": mma_median,
                "deposit_sum": deposit_sum,
                "deposit_avarange": deposit_avarange,
                "deposit_median": deposit_median,
                "value_sum": value_sum,
                "value_avarange": value_avarange,
                "value_median": value_median,
                "tenders": tenders,
                "super_investor": super_investor,
                "super_payment_method": super_payment_method,
                "super_person": super_person,
            }
            return render(request, "archives.html", ctx)


class AddDivisionView(ActivateUserCheck, View):
    def get(self, request):
        counter = get_counter()
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        created_divisions = Division.objects.filter(division_creator=user)
        can_create = 3 - len([i for i in created_divisions])
        form = AddDivisionForm()
        ctx = {
            "form": form,
            "divisions": divisions,
            "created_divisions": created_divisions,
            "can_create": can_create,
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
                        "data": request.POST,
                    }
                    return render(request, "add_division.html", ctx)
            division_name = data["division_name"]
            if request.session.get("user_id") == None:
                ctx = {
                    "form": form,
                    "error_message": "Brak zalogowanego użytkownika",
                    "data": request.POST,
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
            ctx = {"form": form}
            return redirect("/division_choice")


class JoinDivisionView(ActivateUserCheck, View):
    def get(self, request):
        counter = get_counter()
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        wannabe_divisions = Division.objects.filter(division_wannabe=user)
        can_join = 3 - len([i for i in wannabe_divisions])
        form = JoinDivisionForm()
        form.fields["division"].queryset = (
            Division.objects.filter()
            .exclude(division_person=user)
            .exclude(division_wannabe=user)
        )
        ctx = {
            "form": form,
            "divisions": divisions,
            "wannabe_divisions": wannabe_divisions,
            "can_join": can_join,
        }
        return render(request, "join_division.html", ctx)

    def post(self, request):
        form = JoinDivisionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(pk=int(request.session["user_id"]))
            division = data["division"]
            division.division_wannabe.add(user)
            division.save()
            return redirect("/join_division")


class RemoveWannabeView(ActivateUserCheck, View):
    def get(self, request, division_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if division in [i for i in Division.objects.filter(division_wannabe=user)]:
            division.division_wannabe.remove(user)
            division.save()
            return redirect("/join_division")
        return redirect("/projects")


class DivisionChoiceView(ActivateUserCheck, View):
    def get(self, request):
        counter = get_counter()
        user = None
        if request.session["user_id"] not in ("", None):
            user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division_choice = Division.objects.filter(division_person=user)
        ctx = {"division_choice": division_choice, "divisions": divisions}
        return render(request, "division_choice.html", ctx)


class DivisionChoiceConfirm(ActivateUserCheck, View):
    def get(self, request, division_id):
        division = Division.objects.get(pk=division_id)
        user = User.objects.get(pk=request.session.get("user_id"))
        if division in [i for i in user.division_person.all()]:  # url lock
            request.session["division_id"] = division.id
            request.session["division_name"] = division.division_name
            request.session.save()
        return redirect("/projects")


class DivisionDetails(ActivateUserCheck, View):
    def get(self, request, division_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if division in [i for i in user.division_person.all()]:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            actual_projects = Project.objects.filter(division=division, status=2)
            bade_projects = (
                Project.objects.filter(division=division)
                .exclude(status=1)
                .exclude(status=2)
                .exclude(status=3)
            )
            won_projects = Project.objects.filter(division=division, status=5)
            abandoned_projects = Project.objects.filter(division=division, status=3)
            annulled_projects = Project.objects.filter(division=division, status=4)
            exclused_projects = Project.objects.filter(division=division, status=7)
            oldest_project = None
            if bade_projects.count() > 0:
                sorted_bade_projects = sorted(
                    bade_projects, key=lambda x: x.tender_date
                )
                oldest_project = sorted_bade_projects[0]
            ctx = {
                "division": division,
                "divisions": divisions,
                "bade_projects": bade_projects,
                "won_projects": won_projects,
                "abandoned_projects": abandoned_projects,
                "annulled_projects": annulled_projects,
                "actual_projects": actual_projects,
                "exclused_projects": exclused_projects,
                "oldest_project": oldest_project,
            }
            return render(request, "division_details.html", ctx)
        return redirect("/projects")


class DeactivateDivisionView(ActivateUserCheck, View):
    def get(self, request):
        request.session["division_id"] = None
        request.session["division_name"] = None
        request.session.save()
        return redirect("/projects")


class EditDivisionView(StaffMemberCheck, View):
    def get(self, request, division_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if division in [i for i in user.division_admin.all()]:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {"division_name": division.division_name}
            form = EditDivisionForm(initial=initial_data)
            ctx = {"division": division, "form": form, "divisions": divisions}
            return render(request, "edit_division.html", ctx)
        return redirect("/projects")

    def post(self, request, division_id):
        form = EditDivisionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            division = Division.objects.get(id=division_id)
            division.division_name = data["division_name"]
            division.save()
            ctx = {"division": division}
            return redirect(f"/division_details/{division.id}")


class DeleteDivisionView(StaffMemberCheck, View):
    def get(self, request, division_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if division in [i for i in user.division_creator.all()]:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            ctx = {"division": division, "divisions": divisions}
            return render(request, "delete_division.html", ctx)
        return redirect("/projects")


class DeleteDivisionConfirm(StaffMemberCheck, View):
    def get(self, request, division_id):
        division = Division.objects.get(id=division_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if division in [i for i in user.division_creator.all()]:  # url lock
            division.division_company.set([])
            division.delete()
            request.session["division_id"] = None
            request.session["division_name"] = None
            return redirect("/division_choice")
        return redirect("/projects")


class AddAdminView(StaffMemberCheck, View):
    def get(self, request, division_id, person_id):
        division = Division.objects.get(id=division_id)
        person = User.objects.get(id=person_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if (
            division in [i for i in person.division_person.all()]
            and not division in [i for i in person.division_admin.all()]
            and division in [i for i in user.division_creator.all()]
        ):  # url lock
            division.division_admin.add(person)
            division.save()
            person.is_staff = True
            person.save()
            return redirect(f"/division_details/{division.id}")
        return redirect("/projects")


class CancelAdminView(StaffMemberCheck, View):
    def get(self, request, division_id, person_id):
        division = Division.objects.get(id=division_id)
        person = User.objects.get(id=person_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if division in [i for i in person.division_admin.all()] and division in [
            i for i in user.division_creator.all()
        ]:  # url lock
            division.division_admin.remove(person)
            division.save()
            divisions = Division.objects.filter(division_admin=user)
            if len(divisions) == 0:
                user.is_staff = False
                user.save()
            return redirect(f"/division_details/{division.id}")
        return redirect("/projects")


class AddPersonView(StaffMemberCheck, View):
    def get(self, request, division_id, person_id):
        division = Division.objects.get(id=division_id)
        person = User.objects.get(id=person_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if not division in [i for i in person.division_person.all()] and division in [
            i for i in user.division_creator.all()
        ]:  # url lock
            division.division_person.add(person)
            division.division_wannabe.remove(person)
            division.save()
            return redirect(f"/division_details/{division.id}")
        return redirect("/projects")


class RemoveMemberView(StaffMemberCheck, View):
    def get(self, request, division_id, person_id):
        division = Division.objects.get(id=division_id)
        person = User.objects.get(id=person_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        if division in [i for i in person.division_person.all()] and division in [
            i for i in user.division_creator.all()
        ]:  # url lock
            division.division_person.remove(person)
            if person in [i for i in division.division_admin.all()]:
                division.division_admin.remove(person)
            if len(person.division_admin.all()) == 0:
                person.is_staff = False
                person.save()
            division.save()
            return redirect(f"/division_details/{division.id}")
        return redirect("/projects")


class PersonDetailsView(ActivateUserCheck, View):
    def get(self, request, person_id):
        person = User.objects.get(id=person_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        same_division = False
        for i in person.division_person.all():
            if i in user.division_person.all():
                same_division = True
        if same_division:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            division = None
            if request.session.get("division_id"):
                division = Division.objects.get(id=request.session.get("division_id"))
            person_projects = Project.objects.filter(
                person=person, division=division
            ).exclude(status=1)
            person_division_oldest = (
                Project.objects.filter(person=person, division=division)
                .exclude(status=1)
                .exclude(status=2)
                .exclude(status=3)
                .order_by("tender_date")
            )
            person_division_active = Project.objects.filter(
                person=person, division=division, status=2
            )
            person_division_bade = (
                Project.objects.filter(person=person, division=division)
                .exclude(status=1)
                .exclude(status=2)
                .exclude(status=3)
            )
            person_division_won = Project.objects.filter(
                person=person, division=division, status=5
            )
            ctx = {
                "person": person,
                "divisions": divisions,
                "person_projects": person_projects,
                "person_division_oldest": person_division_oldest,
                "person_division_active": person_division_active,
                "person_division_bade": person_division_bade,
                "person_division_won": person_division_won,
            }
            return render(request, "person_details.html", ctx)
        return redirect("/projects")


class UserDetailsView(ActivateUserCheck, View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        division = None
        if request.session.get("division_id"):
            division = Division.objects.get(id=request.session.get("division_id"))
        user_divisions_projects = []
        for i in Division.objects.filter(division_person=user):
            user_divisions_projects.append(
                (
                    i,
                    len(
                        [j for j in i.project_set.filter(person=user).exclude(status=1)]
                    ),
                )
            )
        user_divisions_active = []
        for i in Division.objects.filter(division_person=user):
            user_divisions_active.append(
                (i, len([j for j in i.project_set.filter(person=user, status=2)]))
            )
        user_divisions_bade = []
        for i in Division.objects.filter(division_person=user):
            user_divisions_bade.append(
                (
                    i,
                    len(
                        [
                            j
                            for j in Project.objects.filter(division=i, person=user)
                            .exclude(status=1)
                            .exclude(status=2)
                            .exclude(status=3)
                        ]
                    ),
                )
            )
        user_divisions_oldest = []
        for i in Division.objects.filter(division_person=user):
            user_divisions_oldest.append(
                (
                    i,
                    Project.objects.filter(division=i, person=user)
                    .exclude(status=1)
                    .exclude(status=2)
                    .exclude(status=3)
                    .order_by("tender_date"),
                )
            )
        user_divisions_won = []
        for i in Division.objects.filter(division_person=user):
            user_divisions_won.append(
                (i, len([j for j in i.project_set.filter(person=user, status=5)]))
            )
        user_divisions_abandoned = []
        for i in Division.objects.filter(division_person=user):
            user_divisions_abandoned.append(
                (i, len([j for j in i.project_set.filter(person=user, status=3)]))
            )
        user_divisions_annulled = []
        for i in Division.objects.filter(division_person=user):
            user_divisions_annulled.append(
                (i, len([j for j in i.project_set.filter(person=user, status=4)]))
            )
        user_divisions_exclused = []
        for i in Division.objects.filter(division_person=user):
            user_divisions_exclused.append(
                (i, len([j for j in i.project_set.filter(person=user, status=7)]))
            )
        ctx = {
            "divisions": divisions,
            "user_divisions_projects": user_divisions_projects,
            "user_divisions_oldest": user_divisions_oldest,
            "user_divisions_active": user_divisions_active,
            "user_divisions_bade": user_divisions_bade,
            "user_divisions_won": user_divisions_won,
            "user_divisions_abandoned": user_divisions_abandoned,
            "user_divisions_annulled": user_divisions_annulled,
            "user_divisions_exclused": user_divisions_exclused,
        }
        return render(request, "user_details.html", ctx)


class EditUserView(ActivateUserCheck, View):
    def get(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        initial_data = {"username": user.username}
        form = EditUserForm(initial=initial_data)
        ctx = {"form": form, "divisions": divisions}
        return render(request, "edit_user.html", ctx)

    def post(self, request):
        user = User.objects.get(pk=int(request.session["user_id"]))
        form = EditUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.username = data["username"]
            user.save()
            return redirect(f"/user_details")


class AddTenderView(StaffMemberCheck, View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            form = AddTenderForm()
            ctx = {"project": project, "divisions": divisions, "form": form}
            return render(request, "add_tender.html", ctx)
        return redirect("/projects")

    def post(self, request, project_id):
        user = User.objects.get(pk=int(request.session["user_id"]))
        divisions = [i.id for i in Division.objects.filter(division_admin=user)]
        project = Project.objects.get(id=project_id)
        form = AddTenderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            budget = data["investor_budget"]
            value_weight = data["value_weight"]
            is_guarantee = data["is_guarantee"]
            is_deadline = data["is_deadline"]
            is_other_criteria = data["is_other_criteria"]
            tender = Tender.objects.create(
                investor_budget=budget,
                value_weight=value_weight,
                is_guarantee=is_guarantee,
                is_deadline=is_deadline,
                is_other_criteria=is_other_criteria,
            )
            project.tender = tender
            project.save()
            return redirect(f"/add_tender_criteria/{project.id}/{tender.id}")


class AddTenderCriteria(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id):
        project = Project.objects.get(id=project_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and project.tender.id == tender_id:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            tender = Tender.objects.get(id=tender_id)
            form = AddCriteriaForm(tender=tender)
            ctx = {
                "divisions": divisions,
                "project": project,
                "tender": tender,
                "form": form,
            }
            return render(request, "add_tender_criteria.html", ctx)
        return redirect("/projects")

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
                guarantee = Guarantee.objects.create(
                    weight=guarantee_weight,
                    months_max=guarantee_max,
                    months_min=guarantee_min,
                )
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
                deadline = Deadline.objects.create(
                    weight=deadline_weight,
                    months_min=deadline_min,
                    months_max=deadline_max,
                )
                tender.deadline = deadline
                tender.save()
            criteria = []
            if tender.is_other_criteria:
                criteria = data["criteria"]
                for i in criteria:
                    tender.other_criteria.add(i)
                    tender.save()
            return redirect(f"/add_other_criteria/{project.id}/{tender.id}")


class AddOtherCriteria(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id):
        project = Project.objects.get(id=project_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and project.tender.id == tender_id:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
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
                "count": count,
            }
            return render(request, "add_other_criteria.html", ctx)
        return redirect("/projects")

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
            for i in Criteria.objects.filter(tender=tender):
                if criteria_name in (
                    i.criteria_name,
                    "termin",
                    "Termin",
                    "termin wykonania",
                    "Termin wykonania",
                    "gwarancja",
                    "Gwarancja",
                    "Cena",
                    "cena",
                    "Wartość oferty",
                    "wartość oferty",
                ):
                    return redirect(f"/add_other_criteria/{project_id}/{tender_id}")
            for i in Criteria.objects.all():
                if (
                    criteria_name == i.criteria_name
                    and criteria_weight.weight == i.weight.weight
                ):
                    tender.other_criteria.add(i)
                    tender.save()
                    for i in tender.tenderer.all():
                        new_criteria = Criteria.objects.create(
                            weight=criteria_weight, criteria_name=criteria_name
                        )
                        i.other_criteria.add(new_criteria)
                        i.save()
                    ctx = {
                        "divisions": divisions,
                        "project": project,
                        "tender": tender,
                        "form": form,
                    }
                    return redirect(f"/add_other_criteria/{project_id}/{tender_id}")
            new_criteria = Criteria.objects.create(
                weight=criteria_weight, criteria_name=criteria_name
            )
            tender.other_criteria.add(new_criteria)
            tender.save()
            for i in tender.tenderer.all():
                new_criteria = Criteria.objects.create(
                    weight=criteria_weight, criteria_name=criteria_name
                )
                i.other_criteria.add(new_criteria)
                i.save()
            ctx = {
                "divisions": divisions,
                "project": project,
                "tender": tender,
                "form": form,
            }
            return redirect(f"/add_other_criteria/{project_id}/{tender_id}")


class AddMissingCriteria(StaffMemberCheck, View):
    def post(self, request, project_id, tender_id, criteria_id):
        project = Project.objects.get(id=project_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and project.tender.id == tender_id:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            tender = Tender.objects.get(id=tender_id)
            form_minor = AddMissingCriteriaForm(request.POST, tender=tender)
            if form_minor.is_valid():
                data = form_minor.cleaned_data
                criteria_value = data["criteria_value"]
                criteria = Criteria.objects.get(id=criteria_id)
                criteria.criteria_value = criteria_value
                criteria.save()
                return redirect(f"/add_tender_details/{project.id}/{tender.id}")
        return redirect("/projects")


class AddMissingDeadline(StaffMemberCheck, View):
    def post(self, request, project_id, tender_id, tenderer_id):
        project = Project.objects.get(id=project_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and project.tender.id == tender_id:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            tender = Tender.objects.get(id=tender_id)
            tenderer = Tenderer.objects.get(id=tenderer_id)
            form_deadline = AddMissingDeadlineForm(request.POST, tender=tender)
            if form_deadline.is_valid():
                data = form_deadline.cleaned_data
                deadline = data["deadline"]
                tenderer.offer_deadline = deadline
                tenderer.save()
                return redirect(f"/add_tender_details/{project.id}/{tender.id}")
        return redirect("/projects")


class AddMissingGuarantee(StaffMemberCheck, View):
    def post(self, request, project_id, tender_id, tenderer_id):
        project = Project.objects.get(id=project_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and project.tender.id == tender_id:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            tender = Tender.objects.get(id=tender_id)
            tenderer = Tenderer.objects.get(id=tenderer_id)
            form_guarantee = AddMissingGuaranteeForm(request.POST, tender=tender)
            if form_guarantee.is_valid():
                data = form_guarantee.cleaned_data
                guarantee = data["guarantee"]
                tenderer.offer_guarantee = guarantee
                tenderer.save()
                return redirect(f"/add_tender_details/{project.id}/{tender.id}")
        return redirect("/projects")


class AddTenderDetails(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id):
        project = Project.objects.get(id=project_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and project.tender.id == tender_id:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            tender = Tender.objects.get(id=tender_id)
            form_major = AddTendererForm(tender=tender)
            form_minor = AddMissingCriteriaForm(tender=tender)
            form_deadline = None
            if tender.is_deadline:
                form_deadline = AddMissingDeadlineForm(tender=tender)
            form_guarantee = None
            if tender.is_guarantee:
                form_guarantee = AddMissingGuaranteeForm(tender=tender)

            ctx = {
                "divisions": divisions,
                "project": project,
                "tender": tender,
                "form_major": form_major,
                "form_minor": form_minor,
                "form_deadline": form_deadline,
                "form_guarantee": form_guarantee,
            }
            return render(request, "add_tender_details.html", ctx)
        return redirect("/projects")

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
            tenderer = Tenderer.objects.create(
                tenderer=tenderer,
                offer_value=offer_value,
                offer_guarantee=offer_guarantee,
                offer_deadline=offer_deadline,
            )
            for i in tender.other_criteria.all():
                criteria_value = data.get(f"criteria_value_{i.id}", None)
                criterium = Criteria.objects.create(
                    criteria_name=i.criteria_name,
                    weight=i.weight,
                    criteria_value=criteria_value,
                )
                tenderer.other_criteria.add(criterium)
            if tenderer.tenderer.division_company:
                project.estimated_value = tenderer.offer_value
            tenderer.save()
            tender.tenderer.add(tenderer)
            tender.save()
            status = Status.objects.get(status_name="przegrany")
            project.status = status
            project.save()
            return redirect(f"/add_tender_details/{project.id}/{tender.id}")


class TenderDetailsView(ActivateUserCheck, View):
    def get(self, request, project_id, tender_id):
        project = Project.objects.get(id=project_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and project.tender.id == tender_id:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            tender = Tender.objects.get(id=tender_id)
            winner = None
            rest = None
            for i in tender.tenderer.all():
                if i.is_winner:
                    winner = i
                    break
            tenderers = None
            if winner:
                rest = (
                    tender.tenderer.filter()
                    .exclude(id=winner.id)
                    .order_by("offer_value")
                )
                tenderers = [winner] + [i for i in rest]
            else:
                rest = tender.tenderer.all().order_by("offer_value")
                tenderers = [i for i in rest]
            avarange_price = None
            if Tenderer.objects.filter(tender=tender).count() > 0:
                avarange_price = round(
                    (
                        sum(
                            [
                                i.offer_value
                                for i in Tenderer.objects.filter(tender=tender)
                            ]
                        )
                        / Tenderer.objects.filter(tender=tender).count()
                    ),
                    2,
                )
            ctx = {
                "divisions": divisions,
                "division": division,
                "project": project,
                "tender": tender,
                "winner": winner,
                "tenderers": tenderers,
                "avarange_price": avarange_price,
            }
            return render(request, "tender_details.html", ctx)
        return redirect("/projects")


class MakeWinnerView(View):
    def get(self, request, tender_id, tenderer_id):
        tender = Tender.objects.get(id=tender_id)
        project = Project.objects.get(tender_id=tender_id)
        tenderer = Tenderer.objects.get(id=tenderer_id)
        division = Division.objects.get(pk=int(request.session.get("division_id")))
        if division == project.division and tenderer in [
            i for i in tender.tenderer.all()
        ]:  # url lock
            tenderer.is_winner = True
            tenderer.save()
            if tenderer.tenderer.id == division.division_company.all()[0].id:
                status = Status.objects.get(id=5)
                project.status = status
                project.save()

            return redirect(f"/tender_details/{project.id}/{tender.id}")
        return redirect("/projects")


class RemoveWinnerView(StaffMemberCheck, View):
    def get(self, request, tender_id, tenderer_id):
        tender = Tender.objects.get(id=tender_id)
        project = Project.objects.get(tender_id=tender_id)
        tenderer = Tenderer.objects.get(id=tenderer_id)
        division = Division.objects.get(pk=int(request.session.get("division_id")))
        if division == project.division and tenderer in [
            i for i in tender.tenderer.all()
        ]:  # url lock
            tenderer.is_winner = False
            tenderer.save()
            if tenderer.tenderer.id == division.division_company.all()[0].id:
                status = Status.objects.get(id=6)
                project.status = status
                project.save()
            return redirect(f"/tender_details/{project.id}/{tender.id}")
        return redirect("/projects")


class EditTenderView(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id):
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and tender == project.tender:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {
                "investor_budget": tender.investor_budget,
                "value_weight": tender.value_weight,
                "is_guarantee": tender.is_guarantee,
                "is_deadline": tender.is_deadline,
                "is_other_criteria": tender.is_other_criteria,
            }
            form = EditTenderForm(initial=initial_data)
            ctx = {
                "project": project,
                "tender": tender,
                "divisions": divisions,
                "form": form,
            }
            return render(request, "edit_tender.html", ctx)
        return redirect("/projects")

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
                for i in tender.tenderer.all():
                    i.offer_guarantee = None
                    i.save()
            tender.is_deadline = data["is_deadline"]
            if tender.is_deadline == False:
                tender.deadline = None
                tender.save()
                for i in tender.tenderer.all():
                    i.offer_deadline = None
                    i.save()
            tender.is_other_criteria = data["is_other_criteria"]
            if tender.is_other_criteria == False:
                tender.other_criteria.set([])
                tender.save()
                for i in tender.tenderer.all():
                    i.other_criteria.set([])
                    i.save()
            tender.save()
            return redirect(f"/edit_tender_criteria/{project.id}/{tender.id}")


class EditTenderCriteria(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id):
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and project.tender == tender:  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            initial_data = {}
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
                "form": form,
            }
            return render(request, "edit_tender_criteria.html", ctx)
        return redirect("/projects")

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
                guarantee = Guarantee.objects.create(
                    weight=guarantee_weight,
                    months_max=guarantee_max,
                    months_min=guarantee_min,
                )
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
                deadline = Deadline.objects.create(
                    weight=deadline_weight,
                    months_min=deadline_min,
                    months_max=deadline_max,
                )
                tender.deadline = deadline
                tender.save()
            if tender.is_other_criteria:
                criteria = data["criteria"]
                tender.other_criteria.set(criteria)
                for i in tender.tenderer.all():
                    i.other_criteria.set([])
                    for j in criteria:
                        criterium = Criteria.objects.create(
                            criteria_name=j.criteria_name, weight=j.weight
                        )
                        i.other_criteria.add(criterium)
                        i.save()
                tender.save()
            return redirect(f"/add_other_criteria/{project.id}/{tender.id}")


class DeleteTendererView(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id, tenderer_id):
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        tenderer = Tenderer.objects.get(id=tenderer_id)
        user = User.objects.get(pk=int(request.session["user_id"]))
        division = Division.objects.get(pk=request.session.get("division_id"))
        if (
            division == project.division
            and tender == project.tender
            and tenderer in [i for i in tender.tenderer.all()]
        ):  # url lock
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            tenderer = Tenderer.objects.get(id=tenderer_id)
            criteria = Criteria.objects.filter(tenderer=tenderer)
            for i in criteria:
                i.delete()
            tenderer.delete()
            return redirect(f"/add_tender_details/{project_id}/{tender_id}")
        return redirect("/projects")


class DeleteOtherCriteriaView(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id, criteria_id):
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        criterium = Criteria.objects.get(id=criteria_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if (
            division == project.division
            and tender == project.tender
            and criterium in [i for i in tender.other_criteria.all()]
        ):  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            for i in tender.tenderer.all():
                for j in i.other_criteria.all():
                    if j.criteria_name == criterium.criteria_name:
                        j.delete()
            criterium.delete()
            return redirect(f"/add_other_criteria/{project_id}/{tender_id}")
        return redirect("/projects")


class DeleteTenderView(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id):
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and tender == project.tender:  # url lock
            user = User.objects.get(pk=int(request.session["user_id"]))
            divisions = [i.id for i in Division.objects.filter(division_admin=user)]
            ctx = {"tender": tender, "project": project, "divisions": divisions}
            return render(request, "delete_tender.html", ctx)


class DeleteTenderConfirm(StaffMemberCheck, View):
    def get(self, request, project_id, tender_id):
        project = Project.objects.get(id=project_id)
        tender = Tender.objects.get(id=tender_id)
        division = Division.objects.get(pk=request.session.get("division_id"))
        if division == project.division and tender == project.tender:  # url lock
            criteria = Criteria.objects.filter(tender=tender)
            for i in criteria:
                i.delete()
            tenderers = Tenderer.objects.filter(tender=tender)
            for i in tenderers:
                criteria = Criteria.objects.filter(tenderer=i)
                for j in criteria:
                    j.delete()
                i.delete()
            project.tender = None
            project.save()
            return redirect("/projects")
        return redirect("/projects")
