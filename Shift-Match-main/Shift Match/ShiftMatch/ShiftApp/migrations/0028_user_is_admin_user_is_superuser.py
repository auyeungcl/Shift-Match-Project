# Generated by Django 4.2.7 on 2024-04-01 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftApp', '0027_remove_user_has_module_perms'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
