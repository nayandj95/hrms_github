# Generated by Django 3.0.1 on 2019-12-26 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('roll_user', models.CharField(max_length=25)),
                ('employee_id', models.CharField(max_length=7)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('j_date', models.DateField(auto_now_add=True)),
                ('mobile_no', models.CharField(default='+91', max_length=13)),
                ('department', models.CharField(max_length=25)),
                ('joining_date', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
        ),
    ]