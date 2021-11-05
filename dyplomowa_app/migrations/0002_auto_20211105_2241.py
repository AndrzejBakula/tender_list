# Generated by Django 3.2.3 on 2021-11-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyplomowa_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poviat',
            name='poviat_name',
            field=models.CharField(choices=[(1, 'milicki'), (2, 'oleśnicki'), (3, 'oławski'), (4, 'strzeliński'), (5, 'ząbkowicki'), (6, 'kłodzki'), (7, 'trzebnicki'), (8, 'Wrocław'), (9, 'wrocławski'), (10, 'dzierżoniowski'), (11, 'Wałbrzych'), (12, 'wałbrzyski'), (13, 'świdnicki'), (14, 'średzki'), (15, 'wołowski'), (16, 'górowski'), (17, 'głogowski'), (18, 'polkowicki'), (19, 'lubiński'), (20, 'Legnica'), (21, 'legnicki'), (22, 'jaworski'), (23, 'kamiennogórski'), (24, 'bolesławiecki'), (25, 'złotoryjski'), (26, 'Jelenia Góra'), (27, 'jeleniogórski'), (28, 'zgorzelecki'), (29, 'lubański'), (30, 'Opole'), (31, 'opolski'), (32, 'brzeski'), (33, 'głupczycki'), (34, 'kędzierzyńsko-kozielski'), (35, 'kluczborski'), (36, 'krapkowicki'), (37, 'namysłowski'), (38, 'nyski'), (39, 'oleski'), (40, 'prudnicki'), (41, 'strzelecki'), (42, 'Kalisz'), (43, 'Konin'), (44, 'Leszno'), (45, 'Poznań'), (46, 'chodzieski'), (47, 'czarnkowski-trzcianecki'), (48, 'gnieźnieński'), (49, 'gostyński'), (50, 'grodziski'), (51, 'jarociński'), (52, 'kaliski'), (53, 'kępiński'), (54, 'kolski'), (55, 'koniński'), (56, 'kościański'), (57, 'krotoszyński'), (58, 'leszczyński'), (59, 'międzychodzki'), (60, 'nowotomyski'), (61, 'obornicki'), (62, 'ostrowski'), (63, 'ostrzeszowski'), (64, 'pilski'), (65, 'pleszewski'), (66, 'poznański'), (67, 'rawicki'), (68, 'słupecki'), (69, 'szamotulski'), (70, 'średzki'), (71, 'śremski'), (72, 'turecki'), (73, 'wągrowiecki'), (74, 'wolsztyński'), (75, 'wrzesiński'), (76, 'złotowski'), (77, 'będziński'), (78, 'bielski'), (79, 'Bielsko-Biała'), (80, 'bieruńsko-lędziński'), (81, 'Bytom'), (82, 'Chorzów'), (83, 'cieszyński'), (84, 'Częstochowa'), (85, 'częstochowski'), (86, 'Dąbrowa Górnicza'), (87, 'Gliwice'), (88, 'gliwicki'), (89, 'Jastrzębie-Zdrój'), (90, 'Jaworzno'), (91, 'Katowice'), (92, 'kłobucki'), (93, 'lubliniecki'), (94, 'mikołowski'), (95, 'Mysłowice'), (96, 'myszkowski'), (97, 'Piekary Śląskie'), (98, 'pszczyński'), (99, 'raciborski'), (100, 'Ruda Śląska'), (101, 'rybnicki'), (102, 'Rybnik'), (103, 'Siemanowice Śląskie'), (104, 'Sosnowiec'), (105, 'Świętochłowice'), (106, 'tarnogórski'), (107, 'Tychy'), (108, 'wodzisławski'), (109, 'Zabrze'), (110, 'zawierciański'), (111, 'Żory'), (112, 'żywiecki'), (113, 'Kraków'), (114, 'Nowy Sącz'), (115, 'Tarnów'), (116, 'bocheński'), (117, 'brzeski'), (118, 'chrzanowski'), (119, 'dąbrowski'), (120, 'gorlicki'), (121, 'krakowski'), (122, 'limanowski'), (123, 'miechowski'), (124, 'myślenicki'), (125, 'nowosądecki'), (126, 'nowotarski'), (127, 'olkulski'), (128, 'oświęcimski'), (129, 'proszowicki'), (130, 'suski'), (131, 'tarnowski'), (132, 'tatrzański'), (133, 'wadowicki'), (134, 'wielicki'), (135, 'Rzeszów'), (136, 'Krosno'), (137, 'Przemyśl'), (138, 'Tarnobrzeg'), (139, 'bieszczadzki'), (140, 'brzozowski'), (141, 'dębicki'), (142, 'jarosławski'), (143, 'jasielski'), (144, 'kołbuszowski'), (145, 'krośnieński'), (146, 'leski'), (147, 'leżajski'), (148, 'lubaczowski'), (149, 'łańcucki'), (150, 'mielecki'), (151, 'niżański'), (152, 'przemyski'), (153, 'przeworski'), (154, 'ropczycko-sędziszowski'), (155, 'rzeszowski'), (156, 'sanocki'), (157, 'stalowowolski'), (158, 'strzyżowski'), (159, 'tarnobrzeski'), (160, 'Gorzów Wielkopolski'), (161, 'Zielona Góra'), (162, 'gorzowski'), (163, 'krośnieński (lubuskie)'), (164, 'międzyrzecki'), (165, 'nowosolski'), (166, 'słubicki'), (167, 'strzelecko-drezdenecki'), (168, 'sulęciński'), (169, 'świebodziński'), (170, 'wschowski'), (171, 'zielonogórski'), (172, 'żagański'), (173, 'żarski'), (174, 'Szczecin'), (175, 'Koszalin'), (176, 'Świnoujście'), (177, 'białogardzki'), (178, 'choszczeński'), (179, 'drawski'), (180, 'goleniowski'), (181, 'gryficki'), (182, 'gryfiński'), (183, 'kamieński'), (184, 'kołobrzeski'), (185, 'koszaliński'), (186, 'łobeski'), (187, 'myśliborski'), (188, 'policki'), (189, 'pyrzycki'), (190, 'sławeński'), (191, 'stargardzki'), (192, 'szczecinecki'), (193, 'wałecki'), (194, 'świdwiński'), (195, 'Gdańsk'), (196, 'Gdynia'), (197, 'Słupsk'), (198, 'Sopot'), (199, 'bytowski'), (200, 'chojnicki'), (201, 'człuchowski'), (202, 'kartuski'), (203, 'kościerski'), (204, 'kwidzyński'), (205, 'lęborski'), (206, 'malborski'), (207, 'nowodworski'), (208, 'gdański'), (209, 'pucki'), (210, 'słupski'), (211, 'starogardzki'), (212, 'sztumski'), (213, 'tczewski'), (214, 'wejherowski'), (215, 'Bydgoszcz'), (216, 'Toruń'), (217, 'Włocławek'), (218, 'Grudziądz'), (219, 'aleksandrowski'), (220, 'brodnicki'), (221, 'bydgoski'), (222, 'chełmiński'), (223, 'golubsko-dobrzyński'), (224, 'grudziądzki'), (225, 'inowrocławski'), (226, 'lipnowski'), (227, 'mogileński'), (228, 'nakielski'), (229, 'radziejowski'), (230, 'rypiński'), (231, 'sępoleński'), (232, 'świecki'), (233, 'toruński'), (234, 'tucholski'), (235, 'wąbrzeski'), (236, 'włocławski'), (237, 'żniński'), (238, 'Łódź'), (239, 'Piotrków Trybunalski'), (240, 'Skierniewice'), (241, 'bełchatowski'), (242, 'brzeziński'), (243, 'kutnowski'), (244, 'łaski'), (245, 'łęczycki'), (246, 'łowicki'), (247, 'łódzki wschodni'), (248, 'opoczyński'), (249, 'pabianicki'), (250, 'pajęczański'), (251, 'piotrkowski'), (252, 'poddębicki'), (253, 'radomszczański'), (254, 'rawski'), (255, 'sieradzki'), (256, 'skierniewicki'), (257, 'tomaszowski (łódzkie)'), (258, 'wieruszowski'), (259, 'wieluński'), (260, 'zduńskowolski'), (261, 'zgierski'), (262, 'Lublin'), (263, 'Biała Podlaska'), (264, 'Chełm'), (265, 'Zamość'), (266, 'bialski'), (267, 'biłgorajski'), (268, 'chełmski'), (269, 'hrubieszowski'), (270, 'janowski'), (271, 'krasnostawski'), (272, 'kraśnicki'), (273, 'lubartowski'), (274, 'lubelski'), (275, 'łęczyński'), (276, 'łukowski'), (277, 'opolski'), (278, 'parczewski'), (279, 'puławski'), (280, 'radzyński'), (281, 'rycki'), (282, 'świdnicki'), (283, 'tomaszowski (lubelskie)'), (284, 'włodawski'), (285, 'zamojski'), (286, 'Warszawa'), (287, 'Ostrołęka'), (288, 'Płock'), (289, 'Radom'), (290, 'Siedlce'), (291, 'białobrzeski'), (292, 'ciechanowski'), (293, 'garwoliński'), (294, 'gostyniński'), (295, 'grodziski'), (296, 'grójecki'), (297, 'kozienicki'), (298, 'legionowski'), (299, 'lipski'), (300, 'łosicki'), (301, 'makowski'), (302, 'miński'), (303, 'mławski'), (304, 'nowodworski'), (305, 'ostrołęcki'), (306, 'ostrowski'), (307, 'otwocki'), (308, 'piaseczyński'), (309, 'płocki'), (310, 'płoński'), (311, 'pruszkowski'), (312, 'przasnyski'), (313, 'przysuski'), (314, 'pułtuski'), (315, 'radomski'), (316, 'siedlecki'), (317, 'sierpecki'), (318, 'sochaczewski'), (319, 'sokołowski'), (320, 'szydłowiecki'), (321, 'warszawski zachodni'), (322, 'węgrowski'), (323, 'wołomiński'), (324, 'wyszkowski'), (325, 'zwoleński'), (326, 'żuromiński'), (327, 'żyrardowski'), (328, 'Kielce'), (329, 'buski'), (330, 'jędrzejowski'), (331, 'kazimierski'), (332, 'kielecki'), (333, 'konecki'), (334, 'opatowski'), (335, 'ostrowiecki'), (336, 'pińczowski'), (337, 'sandomierski'), (338, 'skarżyski'), (339, 'starachowicki'), (340, 'staszowski'), (341, 'włoszczowski'), (342, 'Olsztyn'), (343, 'Elbląg'), (344, 'bartoszycki'), (345, 'braniewski'), (346, 'działdowski'), (347, 'elbląski'), (348, 'ełcki'), (349, 'giżycki'), (350, 'gołdapski'), (351, 'iławski'), (352, 'kętrzyński'), (353, 'lidzbarski'), (354, 'mrągowski'), (355, 'nidzicki'), (356, 'nowomiejski'), (357, 'olecki'), (358, 'olsztyński'), (359, 'ostródzki'), (360, 'piski'), (361, 'szczycieński'), (362, 'węgorzewski'), (363, 'Białystok'), (364, 'Łomża'), (365, 'Suwałki'), (366, 'augustowski'), (367, 'białostocki'), (368, 'bielski'), (369, 'grajewski'), (370, 'hajnowski'), (371, 'kolneński'), (372, 'łomżyński'), (373, 'moniecki'), (374, 'sejneński'), (375, 'siemiatycki'), (376, 'sokólski'), (377, 'suwalski'), (378, 'wysokomazowiecki'), (379, 'zambrowski')], max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_number',
            field=models.TextField(default=None, max_length=32, null=True),
        ),
    ]
