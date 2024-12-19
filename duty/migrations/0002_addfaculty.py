# Generated by Django 5.1.4 on 2024-12-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='Male', max_length=100)),
                ('contactNo', models.IntegerField()),
                ('qualification', models.CharField(choices=[('M', 'M.TECH'), ('M', 'MBA'), ('M', 'MCA'), ('M', 'MSC'), ('D', 'DEGREE'), ('B', 'BTECH')], default='M.TECH', max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
