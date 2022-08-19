from datetime import date, timedelta, timezone

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms
from django.contrib.auth.models import User

from .models import (
    AdministrationLevel,
    Company,
    Criteria,
    Designer,
    Division,
    Guarantee,
    Investor,
    Month,
    Note,
    PaymentMethod,
    Poviat,
    Priority,
    Status,
    Tender,
    Voivodeship,
    Weight,
)


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 34, "placeholder": "Nazwa użytkownika"}),
    )
    email = forms.EmailField(
        label="",
        max_length=128,
        widget=forms.EmailInput(attrs={"size": 34, "placeholder": "Adres email"}),
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            {"size": 34, "placeholder": "Hasło"},
        ),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            {"size": 34, "placeholder": "Powtórz hasło"},
        ),
    )
    captcha = ReCaptchaField(
        label="", widget=ReCaptchaV3(attrs={"required_score": 0.85})
    )


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    captcha = ReCaptchaField(
        label="", widget=ReCaptchaV3(attrs={"required_score": 0.85})
    )


class ResetForm(forms.Form):
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            {"size": 34, "placeholder": "Nowe hasło"},
        ),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            {"size": 34, "placeholder": "Powtórz hasło"},
        ),
    )
    captcha = ReCaptchaField(
        label="", widget=ReCaptchaV3(attrs={"required_score": 0.85})
    )


class EditUserForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Użytkownika"}),
    )


class AddInvestorForm(forms.Form):
    investor_name = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Inwestora"}),
    )
    investor_address = forms.CharField(
        label="",
        max_length=256,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Inwestora"}),
    )
    investor_email = forms.EmailField(
        label="",
        max_length=128,
        widget=forms.EmailInput(
            attrs={"size": 34, "placeholder": "Adres email (opcjonalne)"}
        ),
        required=False,
    )
    investor_phone = forms.CharField(
        label="",
        max_length=16,
        widget=forms.TextInput(
            attrs={"size": 24, "placeholder": "Telefon Kontaktowy (opcjonalnie)"}
        ),
        required=False,
    )
    investor_voivodeship = forms.ModelChoiceField(
        label="Województwo", queryset=Voivodeship.objects.all()
    )
    investor_administration_level = forms.ModelChoiceField(
        label="Poziom administracyjny", queryset=AdministrationLevel.objects.all()
    )
    investor_note = forms.ModelChoiceField(
        label="Ocena inwestora", queryset=Note.objects.all(), required=False
    )


class AddInvestorPoviatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        investor = kwargs.get("investor", None)
        kwargs.pop("investor", None)
        self.investor = investor
        super(AddInvestorPoviatForm, self).__init__(*args, **kwargs)
        self.fields["investor_poviat"] = forms.ModelChoiceField(
            label="Powiat",
            queryset=Poviat.objects.filter(
                voivodeship=investor.investor_voivodeship
            ).order_by("poviat_name"),
            required=False,
        )


class EditInvestorForm(forms.Form):
    investor_name = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Inwestora"}),
    )
    investor_address = forms.CharField(
        label="",
        max_length=256,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Inwestora"}),
    )
    investor_email = forms.EmailField(
        label="",
        max_length=128,
        widget=forms.EmailInput(
            attrs={"size": 34, "placeholder": "Adres email (opcjonalne)"}
        ),
        required=False,
    )
    investor_phone = forms.CharField(
        label="",
        max_length=16,
        widget=forms.TextInput(
            attrs={"size": 24, "placeholder": "Telefon Kontaktowy (opcjonalnie)"}
        ),
        required=False,
    )
    investor_voivodeship = forms.ModelChoiceField(
        label="Województwo", queryset=Voivodeship.objects.all()
    )
    investor_administration_level = forms.ModelChoiceField(
        label="Poziom administracyjny", queryset=AdministrationLevel.objects.all()
    )


class EditInvestorPoviatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        investor = kwargs.get("investor", None)
        kwargs.pop("investor", None)
        self.investor = investor
        super(EditInvestorPoviatForm, self).__init__(*args, **kwargs)
        self.fields["investor_poviat"] = forms.ModelChoiceField(
            label="Powiat",
            queryset=Poviat.objects.filter(
                voivodeship=investor.investor_voivodeship
            ).order_by("poviat_name"),
            required=False,
        )


class InvestorNoteForm(forms.Form):
    investor_note = forms.ModelChoiceField(
        label="Ocena inwestora", queryset=Note.objects.all()
    )


class AddCompanyForm(forms.Form):
    company_name = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Firmy"}),
    )
    company_address = forms.CharField(
        label="",
        max_length=256,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Firmy"}),
    )
    company_email = forms.EmailField(
        label="",
        max_length=128,
        widget=forms.EmailInput(
            attrs={"size": 34, "placeholder": "Adres email (opcjonalne)"}
        ),
        required=False,
    )
    company_phone = forms.CharField(
        label="",
        max_length=16,
        widget=forms.TextInput(
            attrs={"size": 24, "placeholder": "Telefon Kontaktowy (opcjonalnie)"}
        ),
        required=False,
    )
    company_contact = forms.CharField(
        label="",
        max_length=64,
        widget=forms.TextInput(
            attrs={"size": 34, "placeholder": "Osoba Kontaktowa (opcjonalnie)"}
        ),
        required=False,
    )
    company_voivodeship = forms.ModelChoiceField(
        label="Województwo", queryset=Voivodeship.objects.all()
    )


class AddCompanyPoviatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        company = kwargs.get("company", None)
        kwargs.pop("company", None)
        self.company = company
        super(AddCompanyPoviatForm, self).__init__(*args, **kwargs)
        self.fields["company_poviat"] = forms.ModelChoiceField(
            label="Powiat",
            queryset=Poviat.objects.filter(
                voivodeship=company.company_voivodeship
            ).order_by("poviat_name"),
            required=False,
        )


class EditCompanyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        company = kwargs.get("company", None)
        kwargs.pop("company", None)
        self.company = company
        super(EditCompanyForm, self).__init__(*args, **kwargs)
        self.fields["company_name"] = forms.CharField(
            label="",
            max_length=128,
            widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Firmy"}),
        )
        self.fields["company_address"] = forms.CharField(
            label="",
            max_length=256,
            widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Firmy"}),
        )
        self.fields["company_email"] = forms.EmailField(
            label="",
            max_length=128,
            widget=forms.EmailInput(
                attrs={"size": 34, "placeholder": "Adres email (opcjonalne)"}
            ),
            required=False,
        )
        self.fields["company_phone"] = forms.CharField(
            label="",
            max_length=16,
            widget=forms.TextInput(
                attrs={"size": 24, "placeholder": "Telefon Kontaktowy (opcjonalnie)"}
            ),
            required=False,
        )
        self.fields["company_contact"] = forms.CharField(
            label="",
            max_length=64,
            widget=forms.TextInput(
                attrs={"size": 34, "placeholder": "Osoba Kontaktowa (opcjonalnie)"}
            ),
            required=False,
        )
        self.fields["company_voivodeship"] = forms.ModelChoiceField(
            label="Województwo", queryset=Voivodeship.objects.all()
        )


class EditCompanyPoviatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        company = kwargs.get("company", None)
        kwargs.pop("company", None)
        self.company = company
        super(EditCompanyPoviatForm, self).__init__(*args, **kwargs)
        self.fields["company_poviat"] = forms.ModelChoiceField(
            label="Powiat",
            queryset=Poviat.objects.filter(
                voivodeship=company.company_voivodeship
            ).order_by("poviat_name"),
            required=False,
        )


class AddDesignerForm(forms.Form):
    designer_name = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Projektanta"}),
    )
    designer_address = forms.CharField(
        label="",
        max_length=256,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Projektanta"}),
    )
    designer_email = forms.EmailField(
        label="",
        max_length=128,
        widget=forms.EmailInput(
            attrs={"size": 34, "placeholder": "Adres email (opcjonalne)"}
        ),
        required=False,
    )
    designer_phone = forms.CharField(
        label="",
        max_length=16,
        widget=forms.TextInput(
            attrs={"size": 24, "placeholder": "Telefon Kontaktowy (opcjonalnie)"}
        ),
        required=False,
    )
    designer_voivodeship = forms.ModelChoiceField(
        label="Województwo",
        queryset=Voivodeship.objects.all().order_by("voivodeship_name"),
    )
    designer_note = forms.ModelChoiceField(
        label="Ocena projektanta", queryset=Note.objects.all(), required=False
    )


class AddDesignerPoviatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        designer = kwargs.get("designer", None)
        kwargs.pop("designer", None)
        self.designer = designer
        super(AddDesignerPoviatForm, self).__init__(*args, **kwargs)
        self.fields["designer_poviat"] = forms.ModelChoiceField(
            label="Powiat",
            queryset=Poviat.objects.filter(
                voivodeship=designer.designer_voivodeship
            ).order_by("poviat_name"),
            required=False,
        )


class DesignerNoteForm(forms.Form):
    designer_note = forms.ModelChoiceField(
        label="Ocena projektanta", queryset=Note.objects.all()
    )


class EditDesignerForm(forms.Form):
    designer_name = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Projektanta"}),
    )
    designer_address = forms.CharField(
        label="",
        max_length=256,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Projektanta"}),
    )
    designer_email = forms.EmailField(
        label="",
        max_length=128,
        widget=forms.EmailInput(
            attrs={"size": 34, "placeholder": "Adres email (opcjonalne)"}
        ),
        required=False,
    )
    designer_phone = forms.CharField(
        label="",
        max_length=16,
        widget=forms.TextInput(
            attrs={"size": 24, "placeholder": "Telefon Kontaktowy (opcjonalnie)"}
        ),
        required=False,
    )
    designer_email = forms.EmailField(
        label="",
        max_length=128,
        widget=forms.EmailInput(
            attrs={"size": 34, "placeholder": "Adres email (opcjonalne)"}
        ),
        required=False,
    )
    designer_voivodeship = forms.ModelChoiceField(
        label="Województwo", queryset=Voivodeship.objects.all()
    )


class EditDesignerPoviatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        designer = kwargs.get("designer", None)
        kwargs.pop("designer", None)
        self.designer = designer
        super(EditDesignerPoviatForm, self).__init__(*args, **kwargs)
        self.fields["designer_poviat"] = forms.ModelChoiceField(
            label="Powiat",
            queryset=Poviat.objects.filter(
                voivodeship=designer.designer_voivodeship
            ).order_by("poviat_name"),
            required=False,
        )


class AddProjectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.get("user", None)
        division = kwargs.get("division", None)
        kwargs.pop("user", None)
        kwargs.pop("division", None)
        self.user = user
        self.division = division
        super(AddProjectForm, self).__init__(*args, **kwargs)
        self.fields["investor"] = forms.ModelChoiceField(
            label="Inwestor",
            queryset=Investor.objects.filter(division=division).order_by(
                "investor_name"
            ),
        )
        self.fields["designer"] = forms.ModelChoiceField(
            label="Projektant",
            required=False,
            queryset=Designer.objects.filter(division=division).order_by(
                "designer_name"
            ),
        )
        self.fields["jv_partners"] = forms.ModelMultipleChoiceField(
            label="Partnerzy konsorcjum",
            queryset=Company.objects.filter(division=division).order_by("company_name"),
            required=False,
        )
        self.fields["person"] = forms.ModelMultipleChoiceField(
            label="Osoba odpowiedzialna",
            required=False,
            queryset=User.objects.filter(division_person=division).order_by("username"),
        )

    project_number = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Numer Projektu"}),
    )
    tender_time = forms.CharField(
        label="Godzina złożenia",
        widget=forms.TextInput(attrs={"type": "time"}),
        required=False,
    )
    open_time = forms.CharField(
        label="Godzina otwarcia",
        widget=forms.TextInput(attrs={"type": "time"}),
        required=False,
    )
    deposit = forms.FloatField(label="Wadium", required=False)
    announcement_number = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Numer ogłoszenia"}),
        required=False,
    )
    announcement_date = forms.CharField(
        label="Data ogłoszenia",
        widget=forms.TextInput(attrs={"type": "date"}),
        required=False,
    )
    voivodeship = forms.ModelChoiceField(
        label="Województwo", queryset=Voivodeship.objects.all()
    )
    tender_date = forms.CharField(
        label="Data złożenia",
        widget=forms.TextInput(attrs={"type": "date"}),
        required=False,
    )
    project_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"size": 56, "placeholder": "Nazwa Projektu"}),
    )
    estimated_value = forms.FloatField(label="Szacunkowa wartość", required=False)
    project_deadline_date = forms.CharField(
        label="Termin realizacji (data)",
        widget=forms.TextInput(attrs={"type": "date"}),
        required=False,
    )
    project_deadline_months = forms.IntegerField(
        label="Termin realizacji (miesiące)", required=False
    )
    project_deadline_days = forms.IntegerField(
        label="Termin realizacji (dni)", required=False
    )
    mma_quantity = forms.IntegerField(label="Ilość MMA [t]", required=False)
    payment_method = forms.ModelChoiceField(
        label="Rozliczenie", queryset=PaymentMethod.objects.all(), required=False
    )
    project_url = forms.URLField(
        label="",
        widget=forms.TextInput(attrs={"size": 56, "placeholder": "Link do przetargu"}),
        required=False,
    )
    rc_date = forms.CharField(
        label="Data komitetu ryzyka",
        widget=forms.TextInput(attrs={"type": "date"}),
        required=False,
    )
    rc_agree = forms.BooleanField(label="Zgoda komitetu ryzyka", required=False)
    evaluation_criteria = forms.CharField(
        label="Kryteria oceny",
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 24,
                "placeholder": "Poszczególne kryteria oddziel przecinkami.",
            }
        ),
        required=False,
    )
    payment_criteria = forms.CharField(
        label="Kryteria płatności",
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 24,
                "placeholder": "Poszczególne kryteria oddziel przecinkami.",
            }
        ),
        required=False,
    )
    remarks = forms.CharField(
        label="Uwagi",
        widget=forms.Textarea(attrs={"rows": 5, "cols": 24, "placeholder": "Uwagi"}),
        required=False,
    )
    priority = forms.ModelChoiceField(
        label="Priorytet", queryset=Priority.objects.all(), required=False
    )
    status = forms.ModelChoiceField(
        label="Status projektu", queryset=Status.objects.all()
    )


class AddProjectPoviatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        project = kwargs.get("project", None)
        kwargs.pop("project", None)
        self.project = project
        super(AddProjectPoviatForm, self).__init__(*args, **kwargs)
        self.fields["poviat"] = forms.ModelChoiceField(
            label="Powiat",
            queryset=Poviat.objects.filter(voivodeship=project.voivodeship).order_by(
                "poviat_name"
            ),
            required=False,
        )


class EditProjectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.get("user", None)
        division = kwargs.get("division", None)
        kwargs.pop("user", None)
        kwargs.pop("division", None)
        self.user = user
        self.division = division
        super(EditProjectForm, self).__init__(*args, **kwargs)
        self.fields["investor"] = forms.ModelChoiceField(
            label="Inwestor",
            queryset=Investor.objects.filter(division=division).order_by(
                "investor_name"
            ),
        )
        self.fields["designer"] = forms.ModelChoiceField(
            label="Projektant",
            required=False,
            queryset=Designer.objects.filter(division=division).order_by(
                "designer_name"
            ),
        )
        self.fields["jv_partners"] = forms.ModelMultipleChoiceField(
            label="Partnerzy konsorcjum",
            queryset=Company.objects.filter(division=division).order_by("company_name"),
            required=False,
        )
        self.fields["person"] = forms.ModelMultipleChoiceField(
            label="Osoba odpowiedzialna",
            required=False,
            queryset=User.objects.filter(division_person=division).order_by("username"),
        )
        self.fields["tender_date"] = forms.CharField(
            label="Data złożenia",
            widget=forms.TextInput(attrs={"type": "date"}),
            required=False,
        )

    project_number = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Numer Projektu"}),
    )
    tender_time = forms.CharField(
        label="Godzina złożenia",
        widget=forms.TextInput(attrs={"type": "time"}),
        required=False,
    )
    open_time = forms.CharField(
        label="Godzina otwarcia",
        widget=forms.TextInput(attrs={"type": "time"}),
        required=False,
    )
    deposit = forms.FloatField(label="Wadium", required=False)
    announcement_number = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Numer ogłoszenia"}),
        required=False,
    )
    announcement_date = forms.CharField(
        label="Data ogłoszenia",
        widget=forms.TextInput(attrs={"type": "date"}),
        required=False,
    )
    voivodeship = forms.ModelChoiceField(
        label="Województwo", queryset=Voivodeship.objects.all()
    )
    project_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"size": 56, "placeholder": "Nazwa Projektu"}),
    )
    estimated_value = forms.FloatField(label="Szacunkowa wartość", required=False)
    project_deadline_date = forms.CharField(
        label="Termin realizacji (data)",
        widget=forms.TextInput(attrs={"type": "date"}),
        required=False,
    )
    project_deadline_months = forms.IntegerField(
        label="Termin realizacji (miesiące)", required=False
    )
    project_deadline_days = forms.IntegerField(
        label="Termin realizacji (dni)", required=False
    )
    mma_quantity = forms.IntegerField(label="Ilość MMA [t]", required=False)
    payment_method = forms.ModelChoiceField(
        label="Rozliczenie", queryset=PaymentMethod.objects.all(), required=False
    )
    project_url = forms.URLField(
        label="",
        widget=forms.TextInput(attrs={"size": 56, "placeholder": "Link do przetargu"}),
        required=False,
    )
    rc_date = forms.CharField(
        label="Data komitetu ryzyka",
        widget=forms.TextInput(attrs={"type": "date"}),
        required=False,
    )
    rc_agree = forms.BooleanField(label="Zgoda komitetu ryzyka", required=False)
    evaluation_criteria = forms.CharField(
        label="Kryteria oceny",
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 24,
                "placeholder": "Poszczególne kryteria oddziel przecinkami.",
            }
        ),
        required=False,
    )
    payment_criteria = forms.CharField(
        label="Kryteria płatności",
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 24,
                "placeholder": "Poszczególne kryteria oddziel przecinkami.",
            }
        ),
        required=False,
    )
    remarks = forms.CharField(
        label="Uwagi",
        widget=forms.Textarea(attrs={"rows": 5, "cols": 24, "placeholder": "Uwagi"}),
        required=False,
    )
    priority = forms.ModelChoiceField(
        label="Priorytet", queryset=Priority.objects.all(), required=False
    )
    status = forms.ModelChoiceField(
        label="Status projektu", queryset=Status.objects.all()
    )


class EditProjectPoviatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        project = kwargs.get("project", None)
        kwargs.pop("project", None)
        self.project = project
        super(EditProjectPoviatForm, self).__init__(*args, **kwargs)
        self.fields["poviat"] = forms.ModelChoiceField(
            label="Powiat",
            queryset=Poviat.objects.filter(voivodeship=project.voivodeship).order_by(
                "poviat_name"
            ),
            required=False,
        )


class SearchProjectForm(forms.Form):
    text = forms.CharField(
        label="Szukany tekst",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "size": 32,
                "placeholder": "Wprowadź fragment nazwy projektu",
            }
        ),
    )


class SearchArchiveForm(forms.Form):
    def __init__(self, *args, **kwargs):
        division = kwargs.get("division", None)
        kwargs.pop("division", None)
        self.division = division
        super(SearchArchiveForm, self).__init__(*args, **kwargs)
        self.fields["text"] = forms.CharField(
            label="Szukany tekst",
            max_length=64,
            widget=forms.TextInput(
                attrs={
                    "size": 34,
                    "placeholder": "Wprowadź fragment nazwy projektu",
                }
            ),
            required=False,
        )
        self.fields["investor"] = forms.ModelChoiceField(
            label="Inwestor",
            queryset=Investor.objects.filter(division=division).order_by(
                "investor_name"
            ),
            required=False,
        )
        self.fields["designer"] = forms.ModelChoiceField(
            label="Projektant",
            queryset=Designer.objects.filter(division=division).order_by(
                "designer_name"
            ),
            required=False,
        )
        self.fields["payment_method"] = forms.ModelChoiceField(
            label="rozliczenie", queryset=PaymentMethod.objects.all(), required=False
        )
        self.fields["person"] = forms.ModelChoiceField(
            label="osoba",
            queryset=User.objects.filter(division_person=division).order_by("username"),
            required=False,
        )
        self.fields["status"] = forms.ModelMultipleChoiceField(
            label="status", queryset=Status.objects.all().exclude(id=2), required=False
        )
        self.fields["date_start"] = forms.DateField(
            label="data od",
            widget=forms.TextInput(attrs={"type": "date"}),
            required=False,
        )
        self.fields["date_end"] = forms.DateField(
            label="data do",
            widget=forms.TextInput(attrs={"type": "date"}),
            required=False,
        )


class SearchInvestorForm(forms.Form):
    text = forms.CharField(
        label="Szukany tekst",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "size": 34,
                "placeholder": "Fragment nazwy inwestora",
            }
        ),
        required=False,
    )
    voivodeship = forms.ModelChoiceField(
        label="Województwo",
        queryset=Voivodeship.objects.all().order_by("voivodeship_name"),
        required=False,
    )
    poviat = forms.ModelChoiceField(
        label="Powiat",
        queryset=Poviat.objects.all().order_by("poviat_name"),
        required=False,
    )
    administration_level = forms.ModelChoiceField(
        label="Poziom administracyjny",
        queryset=AdministrationLevel.objects.all().order_by("level_name"),
        required=False,
    )


class SearchCompanyForm(forms.Form):
    text = forms.CharField(
        label="Szukany tekst",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "size": 34,
                "placeholder": "Wprowadź fragment nazwy firmy",
            }
        ),
        required=False,
    )
    voivodeship = forms.ModelChoiceField(
        label="Województwo",
        queryset=Voivodeship.objects.all().order_by("voivodeship_name"),
        required=False,
    )
    poviat = forms.ModelChoiceField(
        label="Powiat",
        queryset=Poviat.objects.all().order_by("poviat_name"),
        required=False,
    )


class SearchDesignerForm(forms.Form):
    text = forms.CharField(
        label="Szukany tekst",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "size": 34,
                "placeholder": "Wprowadź fragment nazwy projektanta",
            }
        ),
        required=False,
    )
    voivodeship = forms.ModelChoiceField(
        label="Województwo",
        queryset=Voivodeship.objects.all().order_by("voivodeship_name"),
        required=False,
    )
    poviat = forms.ModelChoiceField(
        label="Powiat",
        queryset=Poviat.objects.all().order_by("poviat_name"),
        required=False,
    )


class AddDivisionForm(forms.Form):
    division_name = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Zespołu"}),
    )


class EditDivisionForm(forms.Form):
    division_name = forms.CharField(
        label="",
        max_length=128,
        widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Zespołu"}),
    )


class JoinDivisionForm(forms.Form):
    division = forms.ModelChoiceField(
        label="Wybierz zespół", queryset=Division.objects.all()
    )


class AddTenderForm(forms.Form):
    investor_budget = forms.FloatField(
        label="Budżet inwestora",
        required=False,
        widget=forms.NumberInput(attrs={"step": "0.01"}),
    )
    value_weight = forms.ModelChoiceField(
        label="Waga ceny [%]", queryset=Weight.objects.filter(weight__gt=59)
    )
    is_guarantee = forms.BooleanField(
        label="Czy jest kryterium gwarancji?", required=False
    )
    is_deadline = forms.BooleanField(
        label="Czy jest kryterium terminu wykonania?", required=False
    )
    is_other_criteria = forms.BooleanField(
        label="Czy są jakieś inne kryteria?", required=False
    )


class AddCriteriaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        tender = kwargs.get("tender", None)
        kwargs.pop("tender", None)
        self.tender = tender
        super(AddCriteriaForm, self).__init__(*args, **kwargs)
        if tender.is_guarantee:
            used_weight = 100 - int(tender.value_weight.weight) + 1
            self.fields[f"guarantee_min"] = forms.ModelChoiceField(
                label="Gwarancja min [mies.]",
                queryset=Month.objects.all(),
                required=True,
            )
            self.fields[f"guarantee_max"] = forms.ModelChoiceField(
                label="Gwarancja max [mies.]",
                queryset=Month.objects.all(),
                required=True,
            )
            self.fields[f"guarantee_weight"] = forms.ModelChoiceField(
                label="Waga gwarancji [%]",
                queryset=Weight.objects.filter(weight__lt=used_weight),
                required=True,
            )
        if tender.is_deadline:
            self.fields[f"deadline_min"] = forms.ModelChoiceField(
                label="Termin min [mies.]", queryset=Month.objects.all(), required=True
            )
            self.fields[f"deadline_max"] = forms.ModelChoiceField(
                label="Termin max [mies.]", queryset=Month.objects.all(), required=True
            )
            self.fields[f"deadline_weight"] = forms.ModelChoiceField(
                label="Waga terminu [%]", queryset=Weight.objects.all(), required=True
            )
        if tender.is_other_criteria:
            queryset = (
                Criteria.objects.all()
                .order_by("criteria_name", "weight")
                .distinct("criteria_name", "weight")
            )
            self.fields[f"criteria"] = forms.ModelMultipleChoiceField(
                label="Wybierz inne kryteria oceny", queryset=queryset, required=False
            )


class AddOtherCriteriaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        count = kwargs.get("count", None)
        kwargs.pop("count", None)
        self.count = count
        super(AddOtherCriteriaForm, self).__init__(*args, **kwargs)
        self.fields[f"criteria_name"] = forms.CharField(
            label="",
            max_length=128,
            widget=forms.TextInput(
                attrs={"size": 48, "placeholder": "Nazwa Kryterium"}
            ),
        )
        self.fields[f"criteria_weight"] = forms.ModelChoiceField(
            label="Waga kryterium [%]",
            queryset=Weight.objects.filter(weight__lt=100 - count + 1),
        )


class AddMissingCriteriaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        tender = kwargs.get("tender", None)
        kwargs.pop("tender", None)
        self.tender = tender
        super(AddMissingCriteriaForm, self).__init__(*args, **kwargs)
        self.fields[f"criteria_value"] = forms.CharField(
            label="",
            max_length=64,
            widget=forms.TextInput(attrs={"size": 8, "placeholder": "Wpisz"}),
        )


class AddMissingDeadlineForm(forms.Form):
    def __init__(self, *args, **kwargs):
        tender = kwargs.get("tender", None)
        kwargs.pop("tender", None)
        self.tender = tender
        super(AddMissingDeadlineForm, self).__init__(*args, **kwargs)
        min_dead = int(tender.deadline.months_min.month) - 1
        max_dead = int(tender.deadline.months_max.month) + 1
        self.fields[f"deadline"] = forms.ModelChoiceField(
            label="",
            queryset=Month.objects.filter(month__gt=min_dead, month__lt=max_dead),
        )


class AddMissingGuaranteeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        tender = kwargs.get("tender", None)
        kwargs.pop("tender", None)
        self.tender = tender
        super(AddMissingGuaranteeForm, self).__init__(*args, **kwargs)
        min_guar = int(tender.guarantee.months_min.month) - 1
        max_guar = int(tender.guarantee.months_max.month) + 1
        self.fields[f"guarantee"] = forms.ModelChoiceField(
            label="",
            queryset=Month.objects.filter(month__gt=min_guar, month__lt=max_guar),
        )


class AddTendererForm(forms.Form):
    def __init__(self, *args, **kwargs):
        tender = kwargs.get("tender", None)
        kwargs.pop("tender", None)
        self.tender = tender
        super(AddTendererForm, self).__init__(*args, **kwargs)
        if len(tender.tenderer.all()) > 0:
            excluded_tenderers = [i.tenderer.id for i in tender.tenderer.all()]
            self.fields[f"tenderer"] = forms.ModelChoiceField(
                label="Oferent",
                queryset=Company.objects.filter(division=tender.project.division)
                .exclude(id__in=excluded_tenderers)
                .order_by("company_name"),
            )
        else:
            self.fields[f"tenderer"] = forms.ModelChoiceField(
                label="Oferent",
                queryset=Company.objects.filter(
                    division=tender.project.division
                ).order_by("company_name"),
            )
        self.fields[f"offer_value"] = forms.FloatField(
            label="Wartość oferty brutto",
            widget=forms.NumberInput(attrs={"step": "0.01"}),
        )
        if tender.is_guarantee:
            min_guar = int(tender.guarantee.months_min.month) - 1
            max_guar = int(tender.guarantee.months_max.month) + 1
            self.fields[f"offer_guarantee"] = forms.ModelChoiceField(
                label="Gwarancja",
                queryset=Month.objects.filter(month__gt=min_guar, month__lt=max_guar),
            )
        if tender.is_deadline:
            min_dead = int(tender.deadline.months_min.month) - 1
            max_dead = int(tender.deadline.months_max.month) + 1
            self.fields[f"offer_deadline"] = forms.ModelChoiceField(
                label="Termin wykonania",
                queryset=Month.objects.filter(month__gt=min_dead, month__lt=max_dead),
            )
        if tender.is_other_criteria:
            for i in tender.other_criteria.all():
                self.fields[f"criteria_value_{i.id}"] = forms.CharField(
                    label=f"Wartość kryterium: {i.criteria_name}",
                    max_length=128,
                    widget=forms.TextInput(attrs={"size": 48, "placeholder": ""}),
                )


class EditTenderForm(forms.Form):
    investor_budget = forms.FloatField(
        label="Budżet inwestora",
        required=False,
        widget=forms.NumberInput(attrs={"step": "0.01"}),
    )
    value_weight = forms.ModelChoiceField(
        label="Waga ceny [%]", queryset=Weight.objects.filter(weight__gt=59)
    )
    is_guarantee = forms.BooleanField(
        label="Czy jest kryterium gwarancji?", required=False
    )
    is_deadline = forms.BooleanField(
        label="Czy jest kryterium terminu wykonania?", required=False
    )
    is_other_criteria = forms.BooleanField(
        label="Czy są jakieś inne kryteria?", required=False
    )


class EditCriteriaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        tender = kwargs.get("tender", None)
        kwargs.pop("tender", None)
        self.tender = tender
        super(EditCriteriaForm, self).__init__(*args, **kwargs)
        used_weight = 100 - int(tender.value_weight.weight) + 1
        if tender.is_guarantee:
            self.fields[f"guarantee_min"] = forms.ModelChoiceField(
                label="Gwarancja min [mies.]", queryset=Month.objects.all()
            )
            self.fields[f"guarantee_max"] = forms.ModelChoiceField(
                label="Gwarancja max [mies.]", queryset=Month.objects.all()
            )
            self.fields[f"guarantee_weight"] = forms.ModelChoiceField(
                label="Waga gwarancji [%]",
                queryset=Weight.objects.filter(weight__lt=used_weight),
            )
        if tender.is_deadline:
            self.fields[f"deadline_min"] = forms.ModelChoiceField(
                label="Termin min [mies.]", queryset=Month.objects.all()
            )
            self.fields[f"deadline_max"] = forms.ModelChoiceField(
                label="Termin max [mies.]", queryset=Month.objects.all()
            )
            self.fields[f"deadline_weight"] = forms.ModelChoiceField(
                label="Waga terminu [%]",
                queryset=Weight.objects.filter(weight__lt=used_weight),
            )
        if tender.is_other_criteria:
            queryset = (
                Criteria.objects.all()
                .order_by("criteria_name", "weight")
                .distinct("criteria_name", "weight")
            )
            self.fields[f"criteria"] = forms.ModelMultipleChoiceField(
                label="Wybierz inne kryteria oceny", queryset=queryset, required=False
            )


class EditOtherCriteriaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        count = kwargs.get("count", None)
        kwargs.pop("count", None)
        self.count = count
        super(EditOtherCriteriaForm, self).__init__(*args, **kwargs)
        self.fields[f"criteria_name"] = forms.CharField(
            label="",
            max_length=128,
            widget=forms.TextInput(
                attrs={"size": 48, "placeholder": "Nazwa Kryterium"}
            ),
        )
        self.fields[f"criteria_weight"] = forms.ModelChoiceField(
            label="Waga kryterium [%]",
            queryset=Weight.objects.filter(weight__lt=100 - count + 1),
        )
