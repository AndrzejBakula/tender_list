# Generated by Django 3.2.3 on 2021-11-20 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dyplomowa_app', '0005_auto_20211107_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='tender',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dyplomowa_app.tender'),
        ),
    ]
