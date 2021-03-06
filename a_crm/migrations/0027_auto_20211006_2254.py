# Generated by Django 3.2.6 on 2021-10-06 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('a_crm', '0026_alter_items_agre'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='mana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mana', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер'),
        ),
        migrations.AlterField(
            model_name='items',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='auth', to=settings.AUTH_USER_MODEL, verbose_name='Агент'),
        ),
    ]
