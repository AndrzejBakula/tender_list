# Generated by Django 3.2.3 on 2021-09-19 20:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dyplomowa_app', '0002_division_division_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='division_wannabe',
            field=models.ManyToManyField(related_name='division_wannabe', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='division',
            name='division_admin',
            field=models.ManyToManyField(related_name='division_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='division',
            name='division_person',
            field=models.ManyToManyField(related_name='division_person', to=settings.AUTH_USER_MODEL),
        ),
    ]
