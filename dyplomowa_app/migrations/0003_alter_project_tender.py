# Generated by Django 3.2.3 on 2021-10-22 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dyplomowa_app', '0002_auto_20211020_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tender',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.tender'),
        ),
    ]
