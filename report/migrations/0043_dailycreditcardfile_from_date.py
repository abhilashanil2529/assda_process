# Generated by Django 2.1.2 on 2019-05-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0042_dailycreditcardfile_grand_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailycreditcardfile',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]