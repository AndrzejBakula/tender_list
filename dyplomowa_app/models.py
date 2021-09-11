from django.db import models
from django.contrib.auth.models import User


class AdministrationLevel(models.Model):

    LEVEL = [
        (1, "gminny"),
        (2, "powiatowy"),
        (3, "wojewódzki"),
        (4, "krajowy"),
        (5, "prywatny"),
        (6, "inny")
        ]

    level_name = models.CharField(max_length=32, unique=True, choices=LEVEL)

    def __str__(self):
        return self.level_name


class Note(models.Model):

    NOTE = [
        (1, "brak współpracy"),
        (2, "niska"),
        (3, "średnia"),
        (4, "wysoka")
        ]

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

    PRIORITY = [
        (1, "niski"),
        (2, "średni"),
        (3, "wysoki"),
        (4, "brak")
        ]

    priority_name = models.CharField(max_length=32, unique=True, choices=PRIORITY)

    def __str__(self):
        return self.priority_name


class Status(models.Model):

    STATUS = [
        (1, "brak startu"),
        (2, "w przygotowaniu"),
        (3, "rezygnacja"),
        (4, "unieważniony"),
        (5, "wygrany"),
        (6, "przegrany")
        ]

    status_name = models.CharField(max_length=32, unique=True, choices=STATUS)

    def __str__(self):
        return self.status_name


class PaymentMethod(models.Model):

    PAYMENT_METHOD = [
        (1, "nieokreślono"),
        (2, "ryczałt"),
        (3, "polski ryczałt"),
        (4, "ilościowe"),
        (5, "inne")
        ]

    payment_method_name = models.CharField(max_length=32, unique=True, choices=PAYMENT_METHOD)

    def __str__(self):
        return self.payment_method_name

    
class Division(models.Model):

    DIVISION = [
        (1, "nieokreślono"),
        (2, "Wrocław")
    ]

    division_name = models.CharField(max_length=64, unique=True, choices=DIVISION)

    def __str__(self):
        return self.division_name


class Voivodeship(models.Model):

    VOIVODESHIP = [
        (1, "nieokreślono"),
        (2, "dolnośląskie"),
        (3, "opolskie"),
        (4, "wielkopolskie"),
        (5, "lubuskie"),
        (6, "śląskie"),
        (7, "zachodniopomorskie"),
        (8, "pomorskie"),
        (9, "kujawsko-pomorskie"),
        (10, "warmińsko-mazurskie"),
        (11, "mazowieckie"),
        (12, "łódzkie"),
        (13, "świętokrzyskie"),
        (14, "małopolskie"),
        (15, "podkarpackie"),
        (16, "lubelskie"),
        (17, "podlaskie")
    ]
    POVIAT = [
        ("dolnośląskie", ["milicki", "oleśnicki", "oławski", "strzeliński", "ząbkowicki", "kłodzki",
        "trzebnicki", "Wrocław", "wrocławski", "dzierżoniowski", "Wałbrzych", "wałbrzyski", "świdnicki",
        "średzki", "wołowski", "górowski", "głogowski", "polkowicki", "lubiński", "Legnica", "legnicki",
        "jaworski", "kamiennogórski", "bolesławiecki", "złotoryjski", "Jelenia Góra", "jeleniogórski",
        "zgorzelecki", "lubański"]),
        ("opolskie", []),
        ("wielkopolskie", []),
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

    voivodeship_name = models.CharField(max_length=64, unique=True, choices=VOIVODESHIP)

    poviat = []

    def __str__(self):
        return self.voivodeship_name
    
    def poviats(self):
        for i in POVIAT:
            if self.voivodeship_name == i[0]:
                self.poviat = i[1]
                return None


class JV_Partner(models.Model):

    jv_partner_name  = models.CharField(max_length=64, unique=True)
    jv_partner_address = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.jv_member_name


class Project(models.Model):

    project_number = models.TextField(max_length=32, unique=True, null=True, default=None)
    tender_time = models.TimeField(null=True, default=None)
    open_time = models.TimeField(null=True, default=None)
    deposit = models.FloatField(null=True, default=None)
    announcement_number = models.TextField(default=None, null=True)
    announcement_date = models.DateField(default=None, null=True)
    voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE, default=Voivodeship.VOIVODESHIP[0][0])
    tender_date = models.DateField(null=True, default=None)
    project_name = models.TextField(max_length=512, unique=True)
    estimated_value = models.FloatField(null=True, default=None)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    project_deadline = models.DateField(null=True, default=None)
    mma_quantity = models.IntegerField(null=True, default=None)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, default=PaymentMethod.PAYMENT_METHOD[0][0])
    project_url = models.URLField(unique=True, null=True, default=None)
    person = models.ManyToManyField(User, default=None)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, default=Division.DIVISION[0][0])
    rc_date = models.DateField(null=True, default=None)
    rc_agree = models.BooleanField(null=True, default=None)
    evaluation_criteria = models.TextField(null=True, default=None)
    payment_criteria = models.TextField(null=True, default=None)
    jv_partners = models.ManyToManyField(JV_Partner, default=None)
    remarks = models.TextField(null=True, default=None)
    investor_budget = models.IntegerField(null=True, default=None)

    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=Status.STATUS[0][0])

    def __str__(self):
        return self.project_name




