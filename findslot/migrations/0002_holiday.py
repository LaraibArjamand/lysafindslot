# Generated by Django 3.2.6 on 2021-11-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findslot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('holiday_name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('Weekday', models.DateTimeField()),
            ],
        ),
    ]
