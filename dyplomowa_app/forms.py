from django import forms
from .models import AdministrationLevel, Note, Investor, Designer, Status, Priority
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddInvestorForm(forms.Form):
    investor_name = forms.CharField(
        label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Inwestora"}))
    investor_address = forms.CharField(
        label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Inwestora"}))
    investor_administration_level = forms.ModelChoiceField(
        label="Poziom administracyjny", queryset=AdministrationLevel.objects.all())
    investor_note = forms.ModelChoiceField(label="Ocena inwestora", queryset=Note.objects.all())


class EditInvestorForm(forms.Form):
    investor_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Inwestora"}))
    investor_address = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Inwestora"}))
    investor_administration_level = forms.ModelChoiceField(label="Poziom administracyjny", queryset=AdministrationLevel.objects.all())
    investor_note = forms.ModelChoiceField(label="Ocena inwestora", queryset=Note.objects.all())


class AddDesignerForm(forms.Form):
    designer_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Projektanta"}))
    designer_address = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Projektanta"}))
    designer_note = forms.ModelChoiceField(label="Ocena projektanta", queryset=Note.objects.all())


class EditDesignerForm(forms.Form):
    designer_name = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Projektanta"}))
    designer_address = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"size": 38, "placeholder": "Adres Projektanta"}))
    designer_note = forms.ModelChoiceField(label="Ocena projektanta", queryset=Note.objects.all())


class AddProjectForm(forms.Form):
    project_name = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Projektu"}))
    tender_date = forms.CharField(label="Data złożenia", widget=forms.TextInput(attrs={"type": "date"}))
    investor = forms.ModelChoiceField(label="Inwestor", queryset=Investor.objects.all().order_by("investor_name"))
    estimated_value = forms.FloatField(label="Szacunkowa wartość", required=False)
    deposit = forms.FloatField(label="Wadium", required=False)
    person = forms.ModelMultipleChoiceField(label="Osoba odpowiedzialna", required=False, queryset=User.objects.all().order_by("username"))
    priority = forms.ModelChoiceField(label="Priorytet", queryset=Priority.objects.all())
    designer = forms.ModelChoiceField(label="Projektant", required=False, queryset=Designer.objects.all().order_by("designer_name"))
    status = forms.ModelChoiceField(label="Status projektu", queryset=Status.objects.all())


class EditProjectForm(forms.Form):
    project_name = forms.CharField(label="", widget=forms.TextInput(attrs={"size": 38, "placeholder": "Nazwa Projektu"}))
    tender_date = forms.CharField(label="Data złożenia", widget=forms.TextInput(attrs={"type": "date"}))
    investor = forms.ModelChoiceField(label="Inwestor", queryset=Investor.objects.all().order_by("investor_name"))
    estimated_value = forms.FloatField(label="Szacunkowa wartość", required=False)
    deposit = forms.FloatField(label="Wadium", required=False)
    person = forms.ModelMultipleChoiceField(label="Osoba odpowiedzialna", required=False, queryset=User.objects.all().order_by("username"))
    priority = forms.ModelChoiceField(label="Priorytet", queryset=Priority.objects.all())
    designer = forms.ModelChoiceField(label="Projektant", required=False, queryset=Designer.objects.all().order_by("designer_name"))
    status = forms.ModelChoiceField(label="Status projektu", queryset=Status.objects.all())

