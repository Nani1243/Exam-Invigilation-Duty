# Generated by Django 5.1.4 on 2024-12-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duty', '0006_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddLeisurepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyname', models.CharField(max_length=100)),
                ('examtime', models.CharField(choices=[('9AM-12PM', '9AM-12PM'), ('10AM-13PM', '10AM-13PM'), ('11AM-14PM', '11AM-14PM'), ('12PM-15PM', '12PM-15PM'), ('13PM - 16PM', '13PM - 16PM'), ('14PM - 17PM', '14PM - 17PM'), ('15PM - 16PM', '15PM - 16PM')], max_length=100)),
            ],
        ),
    ]