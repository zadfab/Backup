# Generated by Django 2.2 on 2020-10-03 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20200924_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduler_table',
            name='scheduler_id',
        ),
    ]
