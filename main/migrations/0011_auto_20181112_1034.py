# Generated by Django 2.1.2 on 2018-11-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20181112_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='gsa_commision',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='iata_coordination_fee',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='max_commission_rate',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
