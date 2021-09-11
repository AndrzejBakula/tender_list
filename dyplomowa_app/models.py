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
        (1, "brak"),
        (2, "niski"),
        (3, "średni"),
        (4, "wysoki")
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

    poviats = []
    poviat = None

    def __str__(self):
        return self.voivodeship_name
    
    def set_poviats(self, voivodeship_name):
        for i in POVIAT:
            if voivodeship_name == i[0]:
                self.poviats = i[1]
                return None
    
    def set_poviat(self, poviat):
        self.poviat = poviat
        return None


class Company(models.Model):

    company_name  = models.CharField(max_length=64, unique=True)
    company_address = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.company_name


class Guarantee(models.Model):

    MONTHS = [
        (1, 12), (2, 24), (3, 36), (4, 37), (5, 38), (6, 39), (7, 40), (8, 41), (9, 42), (10, 43), (11, 44),
        (12, 45), (13, 46), (14, 47), (15, 48), (16, 49), (17, 50), (18, 51), (19, 52), (20, 53), (20, 54),
        (21, 55), (22, 56), (23, 57), (24, 58), (25, 59), (26, 60), (27, 61), (28, 62), (29, 63), (30, 64),
        (31, 65), (32, 66), (33, 67), (34, 68), (35, 69), (36, 70), (37, 71), (38, 72), (39, 73), (39, 74),
        (40, 75), (41, 76), (42, 77), (43, 78), (44, 79), (45, 80), (46, 81), (47, 82), (48, 83), (49, 84),
        (50, 85), (51, 86), (52, 87), (53, 88), (54, 89), (55, 90), (56, 91), (57, 92), (58, 93), (59, 94),
        (60, 95), (61, 96), (62, 97), (63, 98), (64, 99), (65, 100), (66, 101), (67, 102), (68, 103),
        (69, 104), (70, 105), (71, 106), (72, 107), (73, 108), (74, 109), (75, 110), (76, 111), (77, 112),
        (78, 113), (79, 114), (80, 115), (81, 116), (82, 117), (83, 118), (84, 119), (85, 120)
    ]

    months = models.IntegerField(unique=True, null=True, default=None, choices=MONTHS)


class Criteria(models.Model):

    criteria_name = models.CharField(max_length=64, unique=True)
    criteria_value = models.TextField(null=True, default=None)

    def __str__(self):
        return self.criteria_name


class Tenderer(models.Model):

    tenderer = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, default=None)
    offer_value = models.FloatField(null=True, default=None)
    offer_guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE, null=True, default=None)
    offer_deadline = models.DateField(null=True, default=None)
    other_criteria = models.ManyToManyField(Criteria, default=None)


class Tender(models.Model):

    investor_budget = models.FloatField(null=True, default=None)
    tenderers = models.ManyToManyField(Tenderer, default=None)


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
    jv_partners = models.ManyToManyField(Company, default=None)
    remarks = models.TextField(null=True, default=None)
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE, null=True, default=None)
    
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, default=Priority.PRIORITY[0][0])
    designer = models.ForeignKey(Designer, null=True, default=None, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=Status.STATUS[0][0])

    def __str__(self):
        return self.project_name




