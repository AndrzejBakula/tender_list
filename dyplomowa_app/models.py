from django.contrib.auth.models import User
from django.db import models


class Counter(models.Model):

    counter = models.IntegerField()

    def __str__(self):
        return str(self.counter)


class Division(models.Model):

    division_name = models.CharField(max_length=64, unique=True)
    division_person = models.ManyToManyField(User, related_name="division_person")
    division_admin = models.ManyToManyField(User, related_name="division_admin")
    division_creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name="division_creator",
    )
    division_wannabe = models.ManyToManyField(User, related_name="division_wannabe")

    def __str__(self):
        return self.division_name


class AdministrationLevel(models.Model):

    LEVEL = [
        (1, "gminny"),
        (2, "powiatowy"),
        (3, "wojewódzki"),
        (4, "krajowy"),
        (5, "prywatny"),
        (6, "inny"),
    ]

    level_name = models.CharField(max_length=32, unique=True, choices=LEVEL)

    def __str__(self):
        return self.level_name


class Note(models.Model):

    NOTE = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    note = models.IntegerField(unique=True, choices=NOTE)
    note_added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, default=None
    )

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
        (17, "podlaskie"),
    ]

    voivodeship_name = models.CharField(max_length=64, unique=True, choices=VOIVODESHIP)

    def __str__(self):
        return self.voivodeship_name


class Poviat(models.Model):

    POVIAT = [
        # DOLNOŚLĄSKIE
        (1, "milicki"),
        (2, "oleśnicki"),
        (3, "oławski"),
        (4, "strzeliński"),
        (5, "ząbkowicki"),
        (6, "kłodzki"),
        (7, "trzebnicki"),
        (8, "Wrocław"),
        (9, "wrocławski"),
        (10, "dzierżoniowski"),
        (11, "Wałbrzych"),
        (12, "wałbrzyski"),
        (13, "świdnicki"),
        (14, "średzki"),
        (15, "wołowski"),
        (16, "górowski"),
        (17, "głogowski"),
        (18, "polkowicki"),
        (19, "lubiński"),
        (20, "Legnica"),
        (21, "legnicki"),
        (22, "jaworski"),
        (23, "kamiennogórski"),
        (24, "bolesławiecki"),
        (25, "złotoryjski"),
        (26, "Jelenia Góra"),
        (27, "karkonoski"),
        (28, "zgorzelecki"),
        (29, "lubański"),
        (380, "lwówecki"),
        # OPOLSKIE
        (30, "Opole"),
        (31, "opolski"),
        (32, "brzeski"),
        (33, "głupczycki"),
        (34, "kędzierzyńsko-kozielski"),
        (35, "kluczborski"),
        (36, "krapkowicki"),
        (37, "namysłowski"),
        (38, "nyski"),
        (39, "oleski"),
        (40, "prudnicki"),
        (41, "strzelecki"),
        # WIELKOPOLSKIE
        (42, "Kalisz"),
        (43, "Konin"),
        (44, "Leszno"),
        (45, "Poznań"),
        (46, "chodzieski"),
        (47, "czarnkowski-trzcianecki"),
        (48, "gnieźnieński"),
        (49, "gostyński"),
        (50, "grodziski"),
        (51, "jarociński"),
        (52, "kaliski"),
        (53, "kępiński"),
        (54, "kolski"),
        (55, "koniński"),
        (56, "kościański"),
        (57, "krotoszyński"),
        (58, "leszczyński"),
        (59, "międzychodzki"),
        (60, "nowotomyski"),
        (61, "obornicki"),
        (62, "ostrowski"),
        (63, "ostrzeszowski"),
        (64, "pilski"),
        (65, "pleszewski"),
        (66, "poznański"),
        (67, "rawicki"),
        (68, "słupecki"),
        (69, "szamotulski"),
        (70, "średzki"),
        (71, "śremski"),
        (72, "turecki"),
        (73, "wągrowiecki"),
        (74, "wolsztyński"),
        (75, "wrzesiński"),
        (76, "złotowski"),
        # ŚLĄSKIE
        (77, "będziński"),
        (78, "bielski"),
        (79, "Bielsko-Biała"),
        (80, "bieruńsko-lędziński"),
        (81, "Bytom"),
        (82, "Chorzów"),
        (83, "cieszyński"),
        (84, "Częstochowa"),
        (85, "częstochowski"),
        (86, "Dąbrowa Górnicza"),
        (87, "Gliwice"),
        (88, "gliwicki"),
        (89, "Jastrzębie-Zdrój"),
        (90, "Jaworzno"),
        (91, "Katowice"),
        (92, "kłobucki"),
        (93, "lubliniecki"),
        (94, "mikołowski"),
        (95, "Mysłowice"),
        (96, "myszkowski"),
        (97, "Piekary Śląskie"),
        (98, "pszczyński"),
        (99, "raciborski"),
        (100, "Ruda Śląska"),
        (101, "rybnicki"),
        (102, "Rybnik"),
        (103, "Siemanowice Śląskie"),
        (104, "Sosnowiec"),
        (105, "Świętochłowice"),
        (106, "tarnogórski"),
        (107, "Tychy"),
        (108, "wodzisławski"),
        (109, "Zabrze"),
        (110, "zawierciański"),
        (111, "Żory"),
        (112, "żywiecki"),
        # MAŁOPOLSKIE
        (113, "Kraków"),
        (114, "Nowy Sącz"),
        (115, "Tarnów"),
        (116, "bocheński"),
        (117, "brzeski"),
        (118, "chrzanowski"),
        (119, "dąbrowski"),
        (120, "gorlicki"),
        (121, "krakowski"),
        (122, "limanowski"),
        (123, "miechowski"),
        (124, "myślenicki"),
        (125, "nowosądecki"),
        (126, "nowotarski"),
        (127, "olkulski"),
        (128, "oświęcimski"),
        (129, "proszowicki"),
        (130, "suski"),
        (131, "tarnowski"),
        (132, "tatrzański"),
        (133, "wadowicki"),
        (134, "wielicki"),
        # PODKARPACKIE
        (135, "Rzeszów"),
        (136, "Krosno"),
        (137, "Przemyśl"),
        (138, "Tarnobrzeg"),
        (139, "bieszczadzki"),
        (140, "brzozowski"),
        (141, "dębicki"),
        (142, "jarosławski"),
        (143, "jasielski"),
        (144, "kołbuszowski"),
        (145, "krośnieński"),
        (146, "leski"),
        (147, "leżajski"),
        (148, "lubaczowski"),
        (149, "łańcucki"),
        (150, "mielecki"),
        (151, "niżański"),
        (152, "przemyski"),
        (153, "przeworski"),
        (154, "ropczycko-sędziszowski"),
        (155, "rzeszowski"),
        (156, "sanocki"),
        (157, "stalowowolski"),
        (158, "strzyżowski"),
        (159, "tarnobrzeski"),
        # LUBUSKIE
        (160, "Gorzów Wielkopolski"),
        (161, "Zielona Góra"),
        (162, "gorzowski"),
        (163, "krośnieński (lubuskie)"),
        (164, "międzyrzecki"),
        (165, "nowosolski"),
        (166, "słubicki"),
        (167, "strzelecko-drezdenecki"),
        (168, "sulęciński"),
        (169, "świebodziński"),
        (170, "wschowski"),
        (171, "zielonogórski"),
        (172, "żagański"),
        (173, "żarski"),
        # ZACHODNIOPOMORSKIE
        (174, "Szczecin"),
        (175, "Koszalin"),
        (176, "Świnoujście"),
        (177, "białogardzki"),
        (178, "choszczeński"),
        (179, "drawski"),
        (180, "goleniowski"),
        (181, "gryficki"),
        (182, "gryfiński"),
        (183, "kamieński"),
        (184, "kołobrzeski"),
        (185, "koszaliński"),
        (186, "łobeski"),
        (187, "myśliborski"),
        (188, "policki"),
        (189, "pyrzycki"),
        (190, "sławeński"),
        (191, "stargardzki"),
        (192, "szczecinecki"),
        (193, "wałecki"),
        (194, "świdwiński"),
        # POMORSKIE
        (195, "Gdańsk"),
        (196, "Gdynia"),
        (197, "Słupsk"),
        (198, "Sopot"),
        (199, "bytowski"),
        (200, "chojnicki"),
        (201, "człuchowski"),
        (202, "kartuski"),
        (203, "kościerski"),
        (204, "kwidzyński"),
        (205, "lęborski"),
        (206, "malborski"),
        (207, "nowodworski"),
        (208, "gdański"),
        (209, "pucki"),
        (210, "słupski"),
        (211, "starogardzki"),
        (212, "sztumski"),
        (213, "tczewski"),
        (214, "wejherowski"),
        # KUJAWSKO-POMORSKIE
        (215, "Bydgoszcz"),
        (216, "Toruń"),
        (217, "Włocławek"),
        (218, "Grudziądz"),
        (219, "aleksandrowski"),
        (220, "brodnicki"),
        (221, "bydgoski"),
        (222, "chełmiński"),
        (223, "golubsko-dobrzyński"),
        (224, "grudziądzki"),
        (225, "inowrocławski"),
        (226, "lipnowski"),
        (227, "mogileński"),
        (228, "nakielski"),
        (229, "radziejowski"),
        (230, "rypiński"),
        (231, "sępoleński"),
        (232, "świecki"),
        (233, "toruński"),
        (234, "tucholski"),
        (235, "wąbrzeski"),
        (236, "włocławski"),
        (237, "żniński"),
        # ŁÓDZKIE
        (238, "Łódź"),
        (239, "Piotrków Trybunalski"),
        (240, "Skierniewice"),
        (241, "bełchatowski"),
        (242, "brzeziński"),
        (243, "kutnowski"),
        (244, "łaski"),
        (245, "łęczycki"),
        (246, "łowicki"),
        (247, "łódzki wschodni"),
        (248, "opoczyński"),
        (249, "pabianicki"),
        (250, "pajęczański"),
        (251, "piotrkowski"),
        (252, "poddębicki"),
        (253, "radomszczański"),
        (254, "rawski"),
        (255, "sieradzki"),
        (256, "skierniewicki"),
        (257, "tomaszowski (łódzkie)"),
        (258, "wieruszowski"),
        (259, "wieluński"),
        (260, "zduńskowolski"),
        (261, "zgierski"),
        # LUBELSKIE
        (262, "Lublin"),
        (263, "Biała Podlaska"),
        (264, "Chełm"),
        (265, "Zamość"),
        (266, "bialski"),
        (267, "biłgorajski"),
        (268, "chełmski"),
        (269, "hrubieszowski"),
        (270, "janowski"),
        (271, "krasnostawski"),
        (272, "kraśnicki"),
        (273, "lubartowski"),
        (274, "lubelski"),
        (275, "łęczyński"),
        (276, "łukowski"),
        (277, "opolski"),
        (278, "parczewski"),
        (279, "puławski"),
        (280, "radzyński"),
        (281, "rycki"),
        (282, "świdnicki"),
        (283, "tomaszowski (lubelskie)"),
        (284, "włodawski"),
        (285, "zamojski"),
        # MAZOWIECKIE
        (286, "Warszawa"),
        (287, "Ostrołęka"),
        (288, "Płock"),
        (289, "Radom"),
        (290, "Siedlce"),
        (291, "białobrzeski"),
        (292, "ciechanowski"),
        (293, "garwoliński"),
        (294, "gostyniński"),
        (295, "grodziski"),
        (296, "grójecki"),
        (297, "kozienicki"),
        (298, "legionowski"),
        (299, "lipski"),
        (300, "łosicki"),
        (301, "makowski"),
        (302, "miński"),
        (303, "mławski"),
        (304, "nowodworski"),
        (305, "ostrołęcki"),
        (306, "ostrowski"),
        (307, "otwocki"),
        (308, "piaseczyński"),
        (309, "płocki"),
        (310, "płoński"),
        (311, "pruszkowski"),
        (312, "przasnyski"),
        (313, "przysuski"),
        (314, "pułtuski"),
        (315, "radomski"),
        (316, "siedlecki"),
        (317, "sierpecki"),
        (318, "sochaczewski"),
        (319, "sokołowski"),
        (320, "szydłowiecki"),
        (321, "warszawski zachodni"),
        (322, "węgrowski"),
        (323, "wołomiński"),
        (324, "wyszkowski"),
        (325, "zwoleński"),
        (326, "żuromiński"),
        (327, "żyrardowski"),
        # ŚWIĘTOKRZYSKIE
        (328, "Kielce"),
        (329, "buski"),
        (330, "jędrzejowski"),
        (331, "kazimierski"),
        (332, "kielecki"),
        (333, "konecki"),
        (334, "opatowski"),
        (335, "ostrowiecki"),
        (336, "pińczowski"),
        (337, "sandomierski"),
        (338, "skarżyski"),
        (339, "starachowicki"),
        (340, "staszowski"),
        (341, "włoszczowski"),
        # WARMIŃSKO-MAZURSKIE
        (342, "Olsztyn"),
        (343, "Elbląg"),
        (344, "bartoszycki"),
        (345, "braniewski"),
        (346, "działdowski"),
        (347, "elbląski"),
        (348, "ełcki"),
        (349, "giżycki"),
        (350, "gołdapski"),
        (351, "iławski"),
        (352, "kętrzyński"),
        (353, "lidzbarski"),
        (354, "mrągowski"),
        (355, "nidzicki"),
        (356, "nowomiejski"),
        (357, "olecki"),
        (358, "olsztyński"),
        (359, "ostródzki"),
        (360, "piski"),
        (361, "szczycieński"),
        (362, "węgorzewski"),
        # PODLASKIE
        (363, "Białystok"),
        (364, "Łomża"),
        (365, "Suwałki"),
        (366, "augustowski"),
        (367, "białostocki"),
        (368, "bielski"),
        (369, "grajewski"),
        (370, "hajnowski"),
        (371, "kolneński"),
        (372, "łomżyński"),
        (373, "moniecki"),
        (374, "sejneński"),
        (375, "siemiatycki"),
        (376, "sokólski"),
        (377, "suwalski"),
        (378, "wysokomazowiecki"),
        (379, "zambrowski"),
    ]

    poviat_name = models.CharField(max_length=64, unique=True, choices=POVIAT)
    voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE)

    def __str__(self):
        return self.poviat_name


class Investor(models.Model):

    investor_name = models.CharField(max_length=128)
    investor_address = models.CharField(max_length=256)
    investor_email = models.EmailField(max_length=64, null=True, default=None)
    investor_phone = models.CharField(max_length=16, null=True, default=None)
    investor_voivodeship = models.ForeignKey(
        Voivodeship, on_delete=models.DO_NOTHING, default=Voivodeship.VOIVODESHIP[0][0]
    )
    investor_poviat = models.ForeignKey(
        Poviat, on_delete=models.DO_NOTHING, null=True, default=None
    )
    investor_administration_level = models.ForeignKey(
        AdministrationLevel, on_delete=models.DO_NOTHING
    )
    investor_note = models.FloatField(max_length=4, null=True, default=None)
    investor_added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    division = models.ManyToManyField(Division)

    def __str__(self):
        return self.investor_name


class InvestorNote(models.Model):

    investor_note_note = models.ForeignKey(Note, on_delete=models.DO_NOTHING)
    investor_note_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    investor_note_investor = models.ForeignKey(Investor, on_delete=models.DO_NOTHING)


class Designer(models.Model):
    designer_name = models.CharField(max_length=128)
    designer_address = models.CharField(max_length=128)
    designer_email = models.EmailField(max_length=64, null=True, default=None)
    designer_phone = models.CharField(max_length=16, null=True, default=None)
    designer_voivodeship = models.ForeignKey(
        Voivodeship, on_delete=models.DO_NOTHING, default=Voivodeship.VOIVODESHIP[0][0]
    )
    designer_poviat = models.ForeignKey(
        Poviat, on_delete=models.DO_NOTHING, null=True, default=None
    )
    designer_note = models.FloatField(max_length=4, null=True, default=None)
    designer_added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    division = models.ManyToManyField(Division)

    def __str__(self):
        return self.designer_name


class DesignerNote(models.Model):

    designer_note_note = models.ForeignKey(Note, on_delete=models.DO_NOTHING)
    designer_note_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    designer_note_designer = models.ForeignKey(Designer, on_delete=models.DO_NOTHING)


class Priority(models.Model):

    PRIORITY = [(1, "brak"), (2, "niski"), (3, "średni"), (4, "wysoki")]

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
        (6, "przegrany"),
        (7, "wykluczenie"),
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
        (5, "inne"),
    ]

    payment_method_name = models.CharField(
        max_length=32, unique=True, choices=PAYMENT_METHOD
    )

    def __str__(self):
        return self.payment_method_name


class Company(models.Model):

    company_name = models.CharField(max_length=64)
    company_address = models.CharField(max_length=128)
    company_voivodeship = models.ForeignKey(
        Voivodeship, on_delete=models.DO_NOTHING, default=Voivodeship.VOIVODESHIP[0][0]
    )
    company_poviat = models.ForeignKey(
        Poviat, on_delete=models.DO_NOTHING, null=True, default=None
    )
    company_added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    division = models.ManyToManyField(Division, related_name="division")
    division_company = models.ForeignKey(
        Division,
        on_delete=models.DO_NOTHING,
        null=True,
        default=None,
        related_name="division_company",
    )

    def __str__(self):
        return self.company_name


class Month(models.Model):

    MONTH = []

    for i in range(360):
        MONTH.append((i + 1, i + 1))

    month = models.IntegerField(unique=True, null=True, default=None, choices=MONTH)

    def __str__(self):
        return str(self.month)


class Weight(models.Model):

    WEIGHT = []

    for i in range(100):
        WEIGHT.append((i + 1, i + 1))

    weight = models.IntegerField(unique=True, null=True, default=None, choices=WEIGHT)

    def __str__(self):
        return str(self.weight)


class Guarantee(models.Model):

    months_min = models.ForeignKey(
        Month, on_delete=models.CASCADE, related_name="guarantee_min"
    )
    months_max = models.ForeignKey(
        Month, on_delete=models.CASCADE, related_name="guarantee_max"
    )
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)


class Deadline(models.Model):

    months_min = models.ForeignKey(
        Month, on_delete=models.CASCADE, related_name="deadline_min"
    )
    months_max = models.ForeignKey(
        Month, on_delete=models.CASCADE, related_name="deadline_max"
    )
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)


class Criteria(models.Model):

    criteria_name = models.CharField(max_length=128)
    criteria_value = models.TextField(null=True, default=None)
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING)
    division = models.ManyToManyField(Division)

    def __str__(self):
        return f"{self.criteria_name} - {self.weight} %"


class Tenderer(models.Model):

    tenderer = models.ForeignKey(Company, on_delete=models.DO_NOTHING, default=None)
    offer_value = models.FloatField(null=True, default=None)
    offer_guarantee = models.ForeignKey(
        Month,
        on_delete=models.DO_NOTHING,
        null=True,
        default=None,
        related_name="offer_guarantee",
    )
    offer_deadline = models.ForeignKey(
        Month,
        on_delete=models.DO_NOTHING,
        null=True,
        default=None,
        related_name="offer_deadline",
    )
    other_criteria = models.ManyToManyField(Criteria, default=None)
    is_winner = models.BooleanField(default=False)


class Tender(models.Model):

    investor_budget = models.FloatField(null=True, default=None)
    tenderer = models.ManyToManyField(Tenderer, default=None)
    value_weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    is_guarantee = models.BooleanField(default=False)
    guarantee = models.ForeignKey(
        Guarantee, on_delete=models.CASCADE, null=True, default=None
    )
    is_deadline = models.BooleanField(default=False)
    deadline = models.ForeignKey(
        Deadline, on_delete=models.CASCADE, null=True, default=None
    )
    is_other_criteria = models.BooleanField(default=False)
    other_criteria = models.ManyToManyField(Criteria, default=None)


class Project(models.Model):

    project_number = models.TextField(max_length=32, null=True, default=None)
    tender_time = models.TimeField(blank=True, null=True)
    open_time = models.TimeField(blank=True, null=True)
    deposit = models.FloatField(null=True, default=None)
    announcement_number = models.TextField(default=None, null=True)
    announcement_date = models.DateField(blank=True, null=True)
    voivodeship = models.ForeignKey(Voivodeship, on_delete=models.DO_NOTHING)
    poviat = models.ForeignKey(
        Poviat, on_delete=models.DO_NOTHING, null=True, default=None
    )
    tender_date = models.DateField(blank=True, null=True)
    project_name = models.TextField(max_length=512)
    estimated_value = models.FloatField(null=True, default=None)
    investor = models.ForeignKey(Investor, on_delete=models.DO_NOTHING)
    project_deadline_date = models.DateField(blank=True, null=True)
    project_deadline_months = models.IntegerField(null=True, default=None)
    project_deadline_days = models.IntegerField(null=True, default=None)
    mma_quantity = models.IntegerField(null=True, default=None)
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.DO_NOTHING, null=True, default=None
    )
    project_url = models.URLField(max_length=500, null=True, default=None)
    person = models.ManyToManyField(User, default=None)
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING)
    rc_date = models.DateField(blank=True, null=True)
    rc_agree = models.BooleanField(null=True, default=None)
    evaluation_criteria = models.TextField(null=True, default=None)
    payment_criteria = models.TextField(null=True, default=None)
    jv_partners = models.ManyToManyField(Company, default=None)
    remarks = models.TextField(null=True, default=None)
    tender = models.OneToOneField(
        Tender, on_delete=models.CASCADE, null=True, default=None
    )
    priority = models.ForeignKey(
        Priority, on_delete=models.DO_NOTHING, null=True, default=None
    )
    designer = models.ForeignKey(
        Designer, null=True, default=None, on_delete=models.DO_NOTHING
    )
    status = models.ForeignKey(
        Status, on_delete=models.DO_NOTHING, default=Status.STATUS[0][0]
    )

    def __str__(self):
        return self.project_name
