# Generated by Django 4.2.7 on 2024-03-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftApp', '0010_shifts_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shifts',
            old_name='user',
            new_name='employeeId',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
