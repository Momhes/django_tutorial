# Generated by Django 2.1 on 2018-08-06 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='inventory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='inventory.Inventory'),
        ),
    ]
