# Generated by Django 3.2.6 on 2021-09-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_per', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titl', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=255, verbose_name='slug')),
                ('desc', models.TextField(blank=True, verbose_name='Описание')),
                ('time_crea', models.DateTimeField(auto_now_add=True)),
                ('time_upda', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организация',
                'ordering': ['titl'],
            },
        ),
    ]
