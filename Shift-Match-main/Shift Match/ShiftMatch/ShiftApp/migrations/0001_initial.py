# Generated by Django 4.2.7 on 2024-02-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('adminPassword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IdRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=100)),
                ('decision', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.EmailField(max_length=254)),
                ('userPassword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('userEmail', models.EmailField(max_length=254)),
                ('employeeId', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('userPassword', models.CharField(max_length=100)),
            ],
        ),
    ]
