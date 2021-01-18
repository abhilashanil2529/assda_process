# Generated by Django 2.1.2 on 2019-02-04 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_airline_accepts_uatp'),
        ('report', '0029_auto_20190204_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportperiod',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_period', to='main.Country'),
        ),
        migrations.AlterUniqueTogether(
            name='reportperiod',
            unique_together={('year', 'month', 'week', 'country')},
        ),
    ]
