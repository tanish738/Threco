# Generated by Django 3.0.14 on 2022-07-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20220718_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='point_of_contact',
            field=models.CharField(choices=[('Sharika Dhar', 'Sharika Dhar'), ('Roocha', 'Roocha')], default='Sharika Dhar', max_length=255),
        ),
    ]
