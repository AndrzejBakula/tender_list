# Generated by Django 3.2.3 on 2021-09-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyplomowa_app', '0002_alter_investor_investor_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='investor_address',
            field=models.CharField(max_length=256),
        ),
    ]
