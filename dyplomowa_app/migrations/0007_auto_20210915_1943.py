# Generated by Django 3.2.3 on 2021-09-15 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dyplomowa_app', '0006_alter_guarantee_months'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poviat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poviat_name', models.CharField(choices=[(1, 'milicki'), (2, 'oleśnicki'), (3, 'oławski'), (4, 'strzeliński'), (5, 'ząbkowicki'), (6, 'kłodzki'), (7, 'trzebnicki'), (8, 'Wrocław'), (9, 'wrocławski'), (10, 'dzierżoniowski'), (11, 'Wałbrzych'), (12, 'wałbrzyski'), (13, 'świdnicki'), (14, 'średzki'), (15, 'wołowski'), (16, 'górowski'), (17, 'głogowski'), (18, 'polkowicki'), (19, 'lubiński'), (20, 'Legnica'), (21, 'legnicki'), (22, 'jaworski'), (23, 'kamiennogórski'), (24, 'bolesławiecki'), (25, 'złotoryjski'), (26, 'Jelenia Góra'), (27, 'jeleniogórski'), (28, 'zgorzelecki'), (29, 'lubański'), (30, 'Opole'), (31, 'opolski'), (32, 'brzeski'), (33, 'głupczycki'), (34, 'kędzierzyńsko-kozielski'), (35, 'kluczborski'), (36, 'krapkowicki'), (37, 'namysłowski'), (38, 'nyski'), (39, 'oleski'), (40, 'prudnicki'), (41, 'strzelecki'), (42, 'Kalisz'), (43, 'Konin'), (44, 'Leszno'), (45, 'Poznań'), (46, 'chodzieski'), (47, 'czarnkowski-trzcianecki'), (48, 'gnieźnieński'), (49, 'gostyński'), (50, 'grodziski'), (51, 'jarociński'), (52, 'kaliski'), (53, 'kępiński'), (54, 'kolski'), (55, 'koniński'), (56, 'kościański'), (57, 'krotoszyński'), (58, 'leszczyński'), (59, 'międzychodzki'), (60, 'nowotomyski'), (61, 'obornicki'), (62, 'ostrowski'), (63, 'ostrzeszowski'), (64, 'pilski'), (65, 'pleszewski'), (66, 'poznański'), (67, 'rawicki'), (68, 'słupecki'), (69, 'szamotulski'), (70, 'średzki'), (71, 'śremski'), (72, 'turecki'), (73, 'wągrowiecki'), (74, 'wolsztyński'), (75, 'wrzesiński'), (76, 'złotowski')], max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='poviat',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dyplomowa_app.poviat'),
        ),
    ]