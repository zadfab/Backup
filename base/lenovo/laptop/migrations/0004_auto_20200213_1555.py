# Generated by Django 2.2 on 2020-02-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0003_remove_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(max_length=20),
        ),
    ]
