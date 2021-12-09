# Generated by Django 3.2.6 on 2021-09-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_crm', '0012_delete_organ'),
    ]

    operations = [
        migrations.AddField(
            model_name='codes',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='codes',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='codes',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='slug'),
        ),
    ]
