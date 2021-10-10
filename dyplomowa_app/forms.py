from django import forms
from .models import AdministrationLevel, Note, Investor, Designer, Status, Priority, Voivodeship, PaymentMethod
from .models import Division, Company, Poviat, Criteria, Guarantee, Weight
from django.contrib.auth.models import User
from datetime import timezone, date, timedelta


class RegisterForm(forms.Form):
    username = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 34, "placeholder": "Nazwa urzytkownika"}))
    email = forms.EmailField(label="", max_length=128, widget=forms.EmailInput(attrs={"size": 34, "placeholder": "Adres email"}))
    password = forms.CharField(label="", widget=forms.PasswordInput({"size": 34, "placeholder": "Hasło"},))
    password2 = forms.CharField(label="", widget=forms.PasswordInput({"size": 34, "placeholder": "Powtórz hasło"},))
    # captcha = ReCaptchaField(label="", widget=ReCaptchaV3(attrs={'required_score':0.85}))


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddInvestorForm(forms.Form):
    investor_name = forms.CharField(
        label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Inwestora"}))
    investor_address = forms.CharField(
        label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Inwestora"}))
    investor_voivodeship = forms.ModelChoiceField(label="Województwo", queryset=Voivodeship.objects.all())
    investor_poviat = forms.ModelChoiceField(label="Powiat", queryset=Poviat.objects.all().order_by("poviat_name"), required=False)
    investor_administration_level = forms.ModelChoiceField(
        label="Poziom administracyjny", queryset=AdministrationLevel.objects.all())
    investor_note = forms.ModelChoiceField(label="Ocena inwestora", queryset=Note.objects.all(), required=False)


class EditInvestorForm(forms.Form):
    investor_name = forms.CharField(
        label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Inwestora"}))
    investor_address = forms.CharField(
        label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Inwestora"}))
    investor_voivodeship = forms.ModelChoiceField(label="Województwo", queryset=Voivodeship.objects.all())
    investor_poviat = forms.ModelChoiceField(label="Powiat", queryset=Poviat.objects.all().order_by("poviat_name"), required=False)
    investor_administration_level = forms.ModelChoiceField(
        label="Poziom administracyjny", queryset=AdministrationLevel.objects.all())


class InvestorNoteForm(forms.Form):
    investor_note = forms.ModelChoiceField(label="Ocena inwestora", queryset=Note.objects.all())


class AddCompanyForm(forms.Form):
    company_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Firmy"}))
    company_address = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Firmy"}))
    company_voivodeship = forms.ModelChoiceField(label="Województwo", queryset=Voivodeship.objects.all())
    company_poviat = forms.ModelChoiceField(label="Powiat", queryset=Poviat.objects.all().order_by("poviat_name"), required=False)


class EditCompanyForm(forms.Form):
    company_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Firmy"}))
    company_address = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Firmy"}))
    company_voivodeship = forms.ModelChoiceField(label="Województwo", queryset=Voivodeship.objects.all())
    company_poviat = forms.ModelChoiceField(label="Powiat", queryset=Poviat.objects.all().order_by("poviat_name"), required=False)

class AddDesignerForm(forms.Form):
    designer_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Projektanta"}))
    designer_address = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Projektanta"}))
    designer_voivodeship = forms.ModelChoiceField(label="Województwo", queryset=Voivodeship.objects.all())
    designer_poviat = forms.ModelChoiceField(label="Powiat", queryset=Poviat.objects.all().order_by("poviat_name"), required=False)
    designer_note = forms.ModelChoiceField(label="Ocena projektanta", queryset=Note.objects.all(), required=False)


class DesignerNoteForm(forms.Form):
    designer_note = forms.ModelChoiceField(label="Ocena projektanta", queryset=Note.objects.all())


class EditDesignerForm(forms.Form):
    designer_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Projektanta"}))
    designer_address = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Projektanta"}))
    designer_voivodeship = forms.ModelChoiceField(label="Województwo", queryset=Voivodeship.objects.all())
    designer_poviat = forms.ModelChoiceField(label="Powiat", queryset=Poviat.objects.all().order_by("poviat_name"), required=False)
    designer_note = forms.ModelChoiceField(label="Ocena projektanta", queryset=Note.objects.all())


class AddProjectForm(forms.Form):
    project_number = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 38, "placeholder": "Numer Projektu"}))
    tender_time = forms.CharField(label="Godzina złożenia", widget=forms.TextInput(attrs={"type": "time"}), required=False)
    open_time = forms.CharField(label="Godzina otwarcia", widget=forms.TextInput(attrs={"type": "time"}), required=False)
    deposit = forms.FloatField(label="Wadium", required=False)
    announcement_number = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 38, "placeholder": "Numer ogłoszenia"}), required=False)
    announcement_date = forms.CharField(label="Data ogłoszenia", widget=forms.TextInput(attrs={"type": "date"}), required=False)
    voivodeship = forms.ModelChoiceField(label="Województwo", queryset=Voivodeship.objects.all())
    poviat = forms.ModelChoiceField(label="Powiat", queryset=Poviat.objects.all().order_by("poviat_name"), required=False)
    tender_date = forms.CharField(label="Data złożenia", widget=forms.TextInput(attrs={"type": "date", 'min': date.today()}), required=False)
    project_name = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 64, "placeholder": "Nazwa Projektu"}))
    estimated_value = forms.FloatField(label="Szacunkowa wartość", required=False)
    investor = forms.ModelChoiceField(label="Inwestor", queryset=Investor.objects.all().order_by("investor_name"))
    project_deadline_date = forms.CharField(label="Termin realizacji (data)", widget=forms.TextInput(attrs={"type": "date", 'min': date.today()}), required=False)
    project_deadline_months = forms.IntegerField(label="Termin realizacji (miesiące)", required=False)
    project_deadline_days = forms.IntegerField(label="Termin realizacji (dni)", required=False)
    mma_quantity = forms.IntegerField(label="Ilość MMA", required=False)
    payment_method = forms.ModelChoiceField(label="Rozliczenie", queryset=PaymentMethod.objects.all(), required=False)
    project_url = forms.URLField(label="", widget=forms.TextInput(attrs={"size": 64, "placeholder": "Link do przetargu"}), required=False)
    person = forms.ModelMultipleChoiceField(label="Osoba odpowiedzialna", required=False, queryset=User.objects.all().order_by("username"))
    division = forms.ModelChoiceField(label="Zespół", queryset=Division.objects.all())
    rc_date = forms.CharField(label="Data komitetu ryzyka", widget=forms.TextInput(attrs={"type": "date"}), required=False)
    rc_agree = forms.BooleanField(label="Zgoda komitetu ryzyka", required=False)
    evaluation_criteria = forms.CharField(label="Kryteria oceny", widget=forms.Textarea(attrs={"rows": 5, "cols": 24, "placeholder": "Kryteria oceny"}), required=False)
    payment_criteria = forms.CharField(label="Kryteria płatności", widget=forms.Textarea(attrs={"rows": 5, "cols": 24, "placeholder": "Kryteria płatności"}), required=False)
    jv_partners = forms.ModelMultipleChoiceField(label="Partnerzy konsorcjum", queryset=Company.objects.all().order_by("company_name"), required=False)
    remarks = forms.CharField(label="Uwagi", widget=forms.Textarea(attrs={"rows": 5, "cols": 24, "placeholder": "Uwagi"}), required=False)
    priority = forms.ModelChoiceField(label="Priorytet", queryset=Priority.objects.all(), required=False)
    designer = forms.ModelChoiceField(label="Projektant", required=False, queryset=Designer.objects.all().order_by("designer_name"))
    status = forms.ModelChoiceField(label="Status projektu", queryset=Status.objects.all())



class EditProjectForm(forms.Form):
    project_number = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 38, "placeholder": "Numer Projektu"}))
    tender_time = forms.CharField(label="Godzina złożenia", widget=forms.TextInput(attrs={"type": "time"}), required=False)
    open_time = forms.CharField(label="Godzina otwarcia", widget=forms.TextInput(attrs={"type": "time"}), required=False)
    deposit = forms.FloatField(label="Wadium", required=False, widget=forms.NumberInput(attrs={'step': "0.01"}))
    announcement_number = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 38, "placeholder": "Numer postępowania"}), required=False)
    announcement_date = forms.CharField(label="Data ogłoszenia", widget=forms.TextInput(attrs={"type": "date"}), required=False)
    voivodeship = forms.ModelChoiceField(label="Województwo", queryset=Voivodeship.objects.all())
    poviat = forms.ModelChoiceField(label="Powiat", queryset=Poviat.objects.all().order_by("poviat_name"), required=False)
    tender_date = forms.CharField(label="Data złożenia", widget=forms.TextInput(attrs={"type": "date", 'min': date.today()}), required=False)
    project_name = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 64, "placeholder": "Nazwa Projektu"}))
    estimated_value = forms.FloatField(label="Szacunkowa wartość", required=False, widget=forms.NumberInput(attrs={'step': "0.01"}))
    investor = forms.ModelChoiceField(label="Inwestor", queryset=Investor.objects.all().order_by("investor_name"))
    project_deadline_date = forms.CharField(label="Termin realizacji (data)", widget=forms.TextInput(attrs={"type": "date", 'min': date.today()}), required=False)
    project_deadline_months = forms.IntegerField(label="Termin realizacji (miesiące)", required=False)
    project_deadline_days = forms.IntegerField(label="Termin realizacji (dni)", required=False)
    mma_quantity = forms.IntegerField(label="Ilość MMA", required=False)
    payment_method = forms.ModelChoiceField(label="Rozliczenie", queryset=PaymentMethod.objects.all(), required=False)
    project_url = forms.URLField(label="", widget=forms.TextInput(attrs={"size": 64, "placeholder": "Link do przetargu"}), required=False)
    person = forms.ModelMultipleChoiceField(label="Osoba odpowiedzialna", required=False, queryset=User.objects.all().order_by("username"))
    division = forms.ModelChoiceField(label="Zespół", queryset=Division.objects.all())
    rc_date = forms.CharField(label="Data komitetu ryzyka", widget=forms.TextInput(attrs={"type": "date"}), required=False)
    rc_agree = forms.BooleanField(label="Zgoda komitetu ryzyka", required=False)
    evaluation_criteria = forms.CharField(label="Kryteria oceny", widget=forms.Textarea(attrs={"rows": 5, "cols": 24, "placeholder": "Kryteria oceny"}), required=False)
    payment_criteria = forms.CharField(label="Kryteria płatności", widget=forms.Textarea(attrs={"rows": 5, "cols": 24, "placeholder": "Kryteria płatności"}), required=False)
    jv_partners = forms.ModelMultipleChoiceField(label="Partnerzy konsorcjum", queryset=Company.objects.all().order_by("company_name"), required=False)
    remarks = forms.CharField(label="Uwagi", widget=forms.Textarea(attrs={"rows": 5, "cols": 24, "placeholder": "Uwagi"}), required=False)
    priority = forms.ModelChoiceField(label="Priorytet", queryset=Priority.objects.all(), required=False)
    designer = forms.ModelChoiceField(label="Projektant", required=False, queryset=Designer.objects.all().order_by("designer_name"))
    status = forms.ModelChoiceField(label="Status projektu", queryset=Status.objects.all())


class SearchProjectForm(forms.Form):
    text = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Wprowadź fragment nazwy projektu i wciśnij enter"}))


class SearchArchiveForm(forms.Form):
    text = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Wprowadź fragment nazwy projektu i wciśnij enter"}))


class SearchInvestorForm(forms.Form):
    text = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"size": 40, "placeholder": "Wprowadź fragment nazwy inwestora i wciśnij enter"}))


class SearchCompanyForm(forms.Form):
    text = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"size": 40, "placeholder": "Wprowadź fragment nazwy firmy i wciśnij enter"}))


class SearchDesignerForm(forms.Form):
    text = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"size": 40, "placeholder": "Wprowadź fragment nazwy projektanta i wciśnij enter"}))


class AddDivisionForm(forms.Form):
    division_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Zespołu"}))


class EditDivisionForm(forms.Form):
    division_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Zespołu"}))


class JoinDivisionForm(forms.Form):
    division = forms.ModelChoiceField(label="Wybierz zespół", queryset=Division.objects.all())

class AddTenderForm(forms.Form):
    investor_budget = forms.FloatField(label="Budżet inwestora", required=False, widget=forms.NumberInput(attrs={'step': "0.01"}))
    value_weight = forms.ModelChoiceField(label="Okreś % wagi ceny", queryset=Weight.objects.all())
    is_guarantee = forms.BooleanField(label="Czy jest kryterium gwarancji?", required=False)
    is_deadline = forms.BooleanField(label="Czy jest kryterium terminu wykonania?", required=False)
    is_other_criteria = forms.BooleanField(label="Czy są jakieś inne kryteria?", required=False)


class ChoiceCriteriaForm(forms.Form):
    criteria = forms.ModelMultipleChoiceField(label="Wybierz inne kryteria oceny", required=False, queryset=Criteria.objects.all().order_by("criteria_name"))


class AddCriteriaForm(forms.Form):
    criteria_name = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Kryterium"}))


class AddTendererForm(forms.Form):
    tenderer = forms.ModelChoiceField(label="Oferent", queryset=Company.objects.all().order_by("company_name"))
    offer_value = forms.FloatField(label="Wartość oferty brutto", required=False, widget=forms.NumberInput(attrs={'step': "0.01"}))
    offer_guarantee = forms.ModelChoiceField(label="Gwarancja", queryset=Guarantee.objects.all())