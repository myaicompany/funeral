# Generated by Django 3.2.6 on 2021-10-06 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('b_per', '0003_rename_midn_persons_phon'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='orga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='b_per.organ', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='persons',
            name='avat',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото пользователя'),
        ),
    ]