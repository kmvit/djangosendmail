# Generated by Django 3.2.13 on 2022-05-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220505_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='operator_code',
            field=models.CharField(editable=False, max_length=3, verbose_name='Код оператора'),
        ),
    ]