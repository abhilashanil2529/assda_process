# Generated by Django 2.1.2 on 2018-11-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20181114_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='code',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]