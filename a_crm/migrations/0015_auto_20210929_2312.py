# Generated by Django 3.2.6 on 2021-09-29 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_crm', '0014_items_coun'),
    ]

    operations = [
        migrations.AddField(
            model_name='codes',
            name='word',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Текстовое отображение цены'),
        ),
        migrations.AlterField(
            model_name='items',
            name='addr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='a_crm.address', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='items',
            name='posi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='a_crm.position', verbose_name='Ориентация'),
        ),
    ]