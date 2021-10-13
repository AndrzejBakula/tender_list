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
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
        ]

    note = models.IntegerField(unique=True, choices=NOTE)
    note_added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"{self.note}"


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

    voivodeship_name = models.CharField(max_length=64, unique=True, choices=VOIVODESHIP)

    def __str__(self):
        return self.voivodeship_name


class Poviat(models.Model):

    POVIAT = [
        #DOLNOŚLĄSKIE
        (1, "milicki"), (2, "oleśnicki"), (3, "oławski"), (4, "strzeliński"), (5, "ząbkowicki"),
        (6, "kłodzki"), (7, "trzebnicki"), (8, "Wrocław"), (9, "wrocławski"), (10, "dzierżoniowski"),
        (11, "Wałbrzych"), (12, "wałbrzyski"), (13, "świdnicki"), (14, "średzki"), (15, "wołowski"),
        (16, "górowski"), (17, "głogowski"), (18, "polkowicki"), (19, "lubiński"), (20, "Legnica"),
        (21, "legnicki"), (22, "jaworski"), (23, "kamiennogórski"), (24, "bolesławiecki"), (25, "złotoryjski"),
        (26, "Jelenia Góra"), (27, "jeleniogórski"), (28, "zgorzelecki"), (29, "lubański"),

        #OPOLSKIE
        (30, "Opole"), (31, "opolski"), (32, "brzeski"), (33, "głupczycki"), (34, "kędzierzyńsko-kozielski"),
        (35, "kluczborski"), (36, "krapkowicki"), (37, "namysłowski"), (38, "nyski"), (39, "oleski"),
        (40, "prudnicki"), (41, "strzelecki"),

        #WIELKOPOLSKIE
        (42, "Kalisz"), (43, "Konin"), (44, "Leszno"), (45, "Poznań"), (46, "chodzieski"),
        (47, "czarnkowski-trzcianecki"), (48, "gnieźnieński"), (49, "gostyński"), (50, "grodziski"),
        (51, "jarociński"), (52, "kaliski"), (53, "kępiński"), (54, "kolski"), (55, "koniński"),
        (56, "kościański"), (57, "krotoszyński"), (58, "leszczyński"), (59, "międzychodzki"), (60, "nowotomyski"),
        (61, "obornicki"), (62, "ostrowski"), (63, "ostrzeszowski"), (64, "pilski"), (65, "pleszewski"),
        (66, "poznański"), (67, "rawicki"), (68, "słupecki"), (69, "szamotulski"), (70, "średzki"),
        (71, "śremski"), (72, "turecki"), (73, "wągrowiecki"), (74, "wolsztyński"), (75, "wrzesiński"),
        (76, "złotowski"),

        #ŚLĄSKIE
        (77, "będziński"), (78, "bielski"), (79, "Bielsko-Biała"), (80, "bieruńsko-lędziński"),
        (81, "Bytom"), (82, "Chorzów"), (83, "cieszyński"), (84, "Częstochowa"), (85, "częstochowski"),
        (86, "Dąbrowa Górnicza"), (87, "Gliwice"), (88, "gliwicki"), (89, "Jastrzębie-Zdrój"),
        (90, "Jaworzno"), (91, "Katowice"), (92, "kłobucki"), (93, "lubliniecki"), (94, "mikołowski"),
        (95, "Mysłowice"), (96, "myszkowski"), (97, "Piekary Śląskie"), (98, "pszczyński"),
        (99, "raciborski"), (100, "Ruda Śląska"), (101, "rybnicki"), (102, "Rybnik"), (103, "Siemanowice Śląskie"),
        (104, "Sosnowiec"), (105, "Świętochłowice"), (106, "tarnogórski"), (107, "Tychy"), (108, "wodzisławski"),
        (109, "Zabrze"), (110, "zawierciański"), (111, "Żory"), (112, "żywiecki")
    ]

    poviat_name = models.CharField(max_length=64, unique=True, choices=POVIAT)

    def __str__(self):
        return self.poviat_name


class Investor(models.Model):

    investor_name = models.CharField(max_length=128, unique=True)
    investor_address = models.CharField(max_length=256)
    investor_voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE, default=Voivodeship.VOIVODESHIP[0][0])
    investor_poviat = models.ForeignKey(Poviat, on_delete=models.CASCADE, null=True, default=None)
    investor_administration_level = models.ForeignKey(AdministrationLevel, on_delete=models.CASCADE)
    investor_note = models.FloatField(max_length=4, null=True, default=None)
    investor_added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.investor_name


class InvestorNote(models.Model):

    investor_note_note = models.ForeignKey(Note, on_delete=models.CASCADE)
    investor_note_user = models.ForeignKey(User, on_delete=models.CASCADE)
    investor_note_investor = models.ForeignKey(Investor, on_delete=models.CASCADE)


class Designer(models.Model):
    designer_name = models.CharField(max_length=128, unique=True)
    designer_address = models.CharField(max_length=128, unique=True)
    designer_voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE, default=Voivodeship.VOIVODESHIP[0][0])
    designer_poviat = models.ForeignKey(Poviat, on_delete=models.CASCADE, null=True, default=None)
    designer_note = models.FloatField(max_length=4, null=True, default=None)
    designer_added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.designer_name


class DesignerNote(models.Model):

    designer_note_note = models.ForeignKey(Note, on_delete=models.CASCADE)
    designer_note_user = models.ForeignKey(User, on_delete=models.CASCADE)
    designer_note_designer = models.ForeignKey(Designer, on_delete=models.CASCADE)


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

    division_name = models.CharField(max_length=64, unique=True)
    division_person = models.ManyToManyField(User, related_name="division_person")
    division_admin = models.ManyToManyField(User, related_name="division_admin")
    division_creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name="division_creator")
    division_wannabe = models.ManyToManyField(User, related_name="division_wannabe")

    def __str__(self):
        return self.division_name


class Company(models.Model):

    company_name  = models.CharField(max_length=64, unique=True)
    company_address = models.CharField(max_length=128, unique=True)
    company_voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE, default=Voivodeship.VOIVODESHIP[0][0])
    company_poviat = models.ForeignKey(Poviat, on_delete=models.CASCADE, null=True, default=None)
    company_added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name


class Month(models.Model):

    MONTH = []

    for i in range(360):
        MONTH.append((i+1, i+1))
    
    month = models.IntegerField(unique=True, null=True, default=None, choices=MONTH)

    def __str__(self):
        return str(self.month)

class Weight(models.Model):

    WEIGHT = []

    for i in range(100):
        WEIGHT.append((i+1, i+1))
    
    weight = models.IntegerField(unique=True, null=True, default=None, choices=WEIGHT)

    def __str__(self):
        return str(self.weight)


class Guarantee(models.Model):

    months_min = models.ForeignKey(Month, on_delete=models.CASCADE, related_name="guarantee_min")
    months_max = models.ForeignKey(Month, on_delete=models.CASCADE, related_name="guarantee_max")
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)


class Deadline(models.Model):

    months_min = models.ForeignKey(Month, on_delete=models.CASCADE, related_name="deadline_min")
    months_max = models.ForeignKey(Month, on_delete=models.CASCADE, related_name="deadline_max")
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)


class Criteria(models.Model):

    criteria_name = models.CharField(max_length=64, unique=True)
    criteria_value = models.TextField(null=True, default=None)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)

    def __str__(self):
        return self.criteria_name


class Tenderer(models.Model):

    tenderer = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, default=None)
    offer_value = models.FloatField(null=True, default=None)
    offer_guarantee = models.ForeignKey(Month, on_delete=models.CASCADE, null=True, default=None, related_name="offer_guarantee")
    offer_deadline = models.ForeignKey(Month, on_delete=models.CASCADE, null=True, default=None, related_name="offer_deadline")
    other_criteria = models.ManyToManyField(Criteria, default=None)


class Tender(models.Model):

    investor_budget = models.FloatField(null=True, default=None)
    tenderer = models.ManyToManyField(Tenderer, default=None)
    value_weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    is_guarantee = models.BooleanField(default=False)
    guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE, null=True, default=None)
    is_deadline = models.BooleanField(default=False)
    deadline = models.ForeignKey(Deadline, on_delete=models.CASCADE, null=True, default=None)
    is_other_criteria = models.BooleanField(default=False)
    other_criteria = models.ManyToManyField(Criteria, default=None)


class Project(models.Model):

    project_number = models.TextField(max_length=32, unique=True, null=True, default=None)
    tender_time = models.TimeField(blank=True, null=True)
    open_time = models.TimeField(blank=True, null=True)
    deposit = models.FloatField(null=True, default=None)
    announcement_number = models.TextField(default=None, null=True)
    announcement_date = models.DateField(blank=True, null=True)
    voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE)
    poviat = models.ForeignKey(Poviat, on_delete=models.CASCADE, null=True, default=None)
    tender_date = models.DateField(blank=True, null=True)
    project_name = models.TextField(max_length=512, unique=True)
    estimated_value = models.FloatField(null=True, default=None)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    project_deadline_date = models.DateField(blank=True, null=True)
    project_deadline_months = models.IntegerField(null=True, default=None)
    project_deadline_days = models.IntegerField(null=True, default=None)
    mma_quantity = models.IntegerField(null=True, default=None)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True, default=None)
    project_url = models.URLField(unique=True, null=True, default=None)
    person = models.ManyToManyField(User, default=None)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    rc_date = models.DateField(blank=True, null=True)
    rc_agree = models.BooleanField(null=True, default=None)
    evaluation_criteria = models.TextField(null=True, default=None)
    payment_criteria = models.TextField(null=True, default=None)
    jv_partners = models.ManyToManyField(Company, default=None)
    remarks = models.TextField(null=True, default=None)
    tender = models.OneToOneField(Tender, on_delete=models.CASCADE, null=True, default=None)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True, default=None)
    designer = models.ForeignKey(Designer, null=True, default=None, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=Status.STATUS[0][0])

    def __str__(self):
        return self.project_name




