# Generated by Django 5.0.6 on 2024-06-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='songdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Song_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Artist_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Genre', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
