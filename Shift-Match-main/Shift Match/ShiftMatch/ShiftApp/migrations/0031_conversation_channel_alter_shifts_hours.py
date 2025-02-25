# Generated by Django 4.2.7 on 2024-04-08 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftApp', '0030_alter_conversation_user_alter_shifts_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='channel',
            field=models.CharField(default='my_channel', max_length=100),
        ),
        migrations.AlterField(
            model_name='shifts',
            name='hours',
            field=models.IntegerField(default=0),
        ),
    ]
