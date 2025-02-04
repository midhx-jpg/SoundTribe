# Generated by Django 5.0.6 on 2024-06-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_songdb_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Venue_hall', models.CharField(blank=True, max_length=50, null=True)),
                ('Venue_address', models.CharField(blank=True, max_length=300, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Event_Image', models.ImageField(blank=True, null=True, upload_to='event_images')),
                ('Description', models.CharField(blank=True, max_length=300, null=True)),
                ('Date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
