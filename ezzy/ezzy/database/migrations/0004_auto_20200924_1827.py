# Generated by Django 2.2 on 2020-09-24 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20200924_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_table',
            name='ezzy_id',
        ),
        migrations.RemoveField(
            model_name='message_forwarding_log',
            name='scheduler_id',
        ),
        migrations.RemoveField(
            model_name='scheduler_table',
            name='scheduler_id',
        ),
        migrations.RemoveField(
            model_name='template_table',
            name='template_id',
        ),
    ]
