# Generated by Django 3.2.6 on 2021-11-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findslot', '0002_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='Weekday',
            field=models.CharField(max_length=25),
        ),
    ]
