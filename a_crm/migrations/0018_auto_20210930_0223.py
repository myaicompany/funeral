# Generated by Django 3.2.6 on 2021-09-29 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_crm', '0017_items_numb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='date_birt',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='items',
            name='date_deat',
            field=models.DateField(blank=True, null=True, verbose_name='Дата смерти'),
        ),
        migrations.AlterField(
            model_name='items',
            name='date_fune',
            field=models.DateField(blank=True, null=True, verbose_name='Дата похорон'),
        ),
    ]
