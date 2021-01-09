# Generated by Django 2.2 on 2020-02-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50)),
                ('mobilenumber', models.CharField(default=' ', max_length=50)),
                ('email', models.CharField(default=' ', max_length=50)),
                ('emailm', models.CharField(default=' ', max_length=50)),
                ('domain', models.CharField(default=' ', max_length=50)),
                ('course', models.CharField(default=' ', max_length=50)),
                ('qualification', models.CharField(default=' ', max_length=50)),
                ('year', models.IntegerField(default=' ')),
                ('city', models.TextField(default=' ', max_length=50)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='student/imagess')),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]