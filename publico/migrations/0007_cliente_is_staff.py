# Generated by Django 5.0.6 on 2024-06-28 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publico', '0006_alter_cliente_managers_cliente_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
