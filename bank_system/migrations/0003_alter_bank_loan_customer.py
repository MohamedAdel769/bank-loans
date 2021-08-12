# Generated by Django 3.2.6 on 2021-08-12 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blnk_main', '0004_remove_loan_app_bank'),
        ('bank_system', '0002_bank_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_loan',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='active_loans', to='blnk_main.customer'),
        ),
    ]
