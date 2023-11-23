# Generated by Django 4.2.7 on 2023-11-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('startdate', models.DateField(max_length=20)),
                ('enddate', models.DateField(max_length=20)),
                ('projectmanager_id', models.IntegerField()),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]