# Generated by Django 2.2 on 2020-09-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('DND_status', models.BooleanField(default=False)),
                ('opt_out_template_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='message_forwarding_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduler_id', models.IntegerField()),
                ('message_id', models.IntegerField()),
                ('email_address', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='scheduler_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduler_id', models.IntegerField()),
                ('time_stamp', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='template_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_id', models.IntegerField()),
                ('template_name', models.CharField(max_length=30)),
                ('template_name_on_cm_com', models.CharField(max_length=30)),
            ],
        ),
    ]