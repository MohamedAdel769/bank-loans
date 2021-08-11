# Generated by Django 3.2.6 on 2021-08-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blnk_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan_app',
            name='loan_term',
        ),
        migrations.AlterField(
            model_name='loan_app',
            name='app_type',
            field=models.CharField(choices=[('Fund', 'Fund'), ('Loan', 'Loan')], default='Loan', max_length=10),
        ),
    ]
