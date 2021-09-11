from django.db import models
from django.contrib.auth.models import User


class AdministrationLevel(models.Model):

    LEVEL = [(1, "gminny"), (2, "powiatowy"), (3, "wojewódzki"), (4, "krajowy"), (5, "prywatny"), (6, "inny")]

    level_name = models.CharField(max_length=32, unique=True, choices=LEVEL)

    def __str__(self):
        return self.level_name


class Note(models.Model):

    NOTE = [(1, "brak współpracy"), (2, "niska"), (3, "średnia"), (4, "wysoka")]

    note = models.CharField(max_length=32, unique=True, choices=NOTE)

    def __str__(self):
        return self.note


class Investor(models.Model):

    investor_name = models.CharField(max_length=128, unique=True)
    investor_address = models.CharField(max_length=256, unique=True)
    investor_administration_level = models.ForeignKey(AdministrationLevel, on_delete=models.CASCADE)
    investor_note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.investor_name


class Designer(models.Model):
    designer_name = models.CharField(max_length=128, unique=True)
    designer_address = models.CharField(max_length=128, unique=True)
    designer_note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.designer_name


class Priority(models.Model):

    PRIORITY = [(1, "niski"), (2, "średni"), (3, "wysoki"), (4, "brak")]

    priority_name = models.CharField(max_length=32, unique=True, choices=PRIORITY)

    def __str__(self):
        return self.priority_name


class Status(models.Model):

    STATUS = [(1, "brak startu"), (2, "w przygotowaniu"), (3, "rezygnacja"), (4, "unieważniony"), (5, "wygrany"), (6, "przegrany")]

    status_name = models.CharField(max_length=32, unique=True, default="brak startu", choices=STATUS)

    def __str__(self):
        return self.status_name


class Project(models.Model):

    VOIVODESHIP = [
        (1, "dolnośląskie"),
        (2, "opolskie"),
        (3, "wielkopolskie"),
        (4, "lubuskie"),
        (5, "śląskie"),
        (6, "zachodniopomorskie"),
        (7, "pomorskie"),
        (8, "kujawsko-pomorskie"),
        (9, "warmińsko-mazurskie"),
        (10, "mazowieckie"),
        (11, "łódzkie"),
        (12, "świętokrzyskie"),
        (13, "małopolskie"),
        (14, "podkarpackie"),
        (15, "lubelskie"),
        (16, "podlaskie")
    ]

    project_number = models.TextField(max_length=32, unique=True, null=True)
    project_name = models.TextField(max_length=512, unique=True)
    tender_date = models.DateField()
    tender_time = models.TimeField(null=True, default=None)
    open_time = models.TimeField(null=True, default=None)
    deposit = models.FloatField(null=True)
    announcement_number = models.TextField(unique=True, default=None, null=True)
    announcement_date = models.DateField(unique=True, default=None, null=True)
    voivodeship = models.TextField(default=None, null=True, choices=VOIVODESHIP)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    estimated_value = models.FloatField(null=True)

    person = models.ManyToManyField(User)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name




