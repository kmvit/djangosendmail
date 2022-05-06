# Generated by Django 3.2.13 on 2022-05-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='mobile_operator_code',
            field=models.CharField(blank=True, max_length=3, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='tag',
            field=models.CharField(blank=True, max_length=100, verbose_name='Tags'),
        ),
    ]
