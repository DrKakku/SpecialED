# Generated by Django 3.0.3 on 2020-02-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='disability',
            name='pic',
            field=models.ImageField(default='blindkid.jpg', upload_to='Disability/'),
        ),
    ]
