# Generated by Django 3.2.6 on 2021-09-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='date_fune',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Дата похорон'),
        ),
    ]