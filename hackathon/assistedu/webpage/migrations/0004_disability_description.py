# Generated by Django 3.0.3 on 2020-02-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_disability_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='disability',
            name='description',
            field=models.CharField(default='hello', max_length=200),
        ),
    ]
