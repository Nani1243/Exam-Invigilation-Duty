# Generated by Django 5.1.1 on 2025-01-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duty', '0015_rename_facultyname_addleisurepage_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addleisurepage',
            name='available',
        ),
        migrations.AddField(
            model_name='addleisurepage',
            name='facultyname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
