# Generated by Django 4.2.7 on 2024-03-20 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftApp', '0016_shifts_shifthourend_shifts_shifthourstart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shifts',
            name='shiftHourEnd',
        ),
        migrations.RemoveField(
            model_name='shifts',
            name='shiftHourStart',
        ),
    ]
