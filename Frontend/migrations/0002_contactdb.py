# Generated by Django 5.0.6 on 2024-07-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Subject', models.CharField(blank=True, max_length=200, null=True)),
                ('Message', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
