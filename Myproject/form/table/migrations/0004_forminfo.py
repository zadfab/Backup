# Generated by Django 2.2 on 2020-03-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_auto_20200316_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='forminfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
            ],
        ),
    ]
