# Generated by Django 3.2.3 on 2021-11-07 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dyplomowa_app', '0004_auto_20211107_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_poviat',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.poviat'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_voivodeship',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.voivodeship'),
        ),
        migrations.AlterField(
            model_name='company',
            name='division_company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='division_company', to='dyplomowa_app.division'),
        ),
        migrations.AlterField(
            model_name='criteria',
            name='weight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.weight'),
        ),
        migrations.AlterField(
            model_name='designer',
            name='designer_added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='designer',
            name='designer_poviat',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.poviat'),
        ),
        migrations.AlterField(
            model_name='designer',
            name='designer_voivodeship',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.voivodeship'),
        ),
        migrations.AlterField(
            model_name='designernote',
            name='designer_note_designer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.designer'),
        ),
        migrations.AlterField(
            model_name='designernote',
            name='designer_note_note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.note'),
        ),
        migrations.AlterField(
            model_name='designernote',
            name='designer_note_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='investornote',
            name='investor_note_investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.investor'),
        ),
        migrations.AlterField(
            model_name='investornote',
            name='investor_note_note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.note'),
        ),
        migrations.AlterField(
            model_name='project',
            name='designer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.designer'),
        ),
        migrations.AlterField(
            model_name='project',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.division'),
        ),
        migrations.AlterField(
            model_name='project',
            name='investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.investor'),
        ),
        migrations.AlterField(
            model_name='project',
            name='payment_method',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.paymentmethod'),
        ),
        migrations.AlterField(
            model_name='project',
            name='poviat',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.poviat'),
        ),
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.priority'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.status'),
        ),
        migrations.AlterField(
            model_name='project',
            name='voivodeship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.voivodeship'),
        ),
        migrations.AlterField(
            model_name='tenderer',
            name='offer_deadline',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_deadline', to='dyplomowa_app.month'),
        ),
        migrations.AlterField(
            model_name='tenderer',
            name='offer_guarantee',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_guarantee', to='dyplomowa_app.month'),
        ),
        migrations.AlterField(
            model_name='tenderer',
            name='tenderer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='dyplomowa_app.company'),
        ),
    ]
