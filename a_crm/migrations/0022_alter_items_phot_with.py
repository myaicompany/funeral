# Generated by Django 3.2.6 on 2021-09-29 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_crm', '0021_alter_items_phot_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='phot_with',
            field=models.BooleanField(blank=True, null=True, verbose_name='С фото?'),
        ),
    ]
