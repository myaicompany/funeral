# Generated by Django 3.2.6 on 2021-10-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_crm', '0027_auto_20211006_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='codes',
            name='phot',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
