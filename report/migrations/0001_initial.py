# Generated by Django 2.1.2 on 2018-11-05 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agency', '0004_auto_20181031_1312'),
        ('main', '0006_country_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyDebitMemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('fare', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='reportfile')),
                ('file_date', models.DateField(null=True)),
                ('ref_no', models.CharField(max_length=10, null=True)),
                ('imported_at', models.DateTimeField(auto_now_add=True)),
                ('net_sales', models.FloatField(null=True)),
                ('gross_sales', models.FloatField(null=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='ReportPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.SmallIntegerField()),
                ('week', models.SmallIntegerField()),
                ('ped', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('type', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('card_no', models.CharField(max_length=4, null=True)),
                ('value', models.FloatField(null=True)),
                ('rate', models.FloatField(null=True)),
                ('international_flag', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bank_code', models.CharField(max_length=20)),
                ('sales_total', models.FloatField(null=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.Agency')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportFile')),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='transaction',
            field=models.ManyToManyField(to='report.Transaction'),
        ),
        migrations.AddField(
            model_name='taxes',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Ticket'),
        ),
        migrations.AlterUniqueTogether(
            name='reportperiod',
            unique_together={('year', 'month', 'week')},
        ),
        migrations.AddField(
            model_name='reportfile',
            name='report_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportPeriod'),
        ),
        migrations.AddField(
            model_name='charges',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Ticket'),
        ),
        migrations.AddField(
            model_name='agencydebitmemo',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Ticket'),
        ),
    ]