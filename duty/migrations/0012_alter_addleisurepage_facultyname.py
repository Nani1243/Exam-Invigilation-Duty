# Generated by Django 5.1.1 on 2025-01-05 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duty', '0011_delete_invigilation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addleisurepage',
            name='facultyname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duty.addfaculty'),
        ),
    ]
