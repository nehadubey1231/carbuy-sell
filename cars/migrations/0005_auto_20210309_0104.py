# Generated by Django 3.0.7 on 2021-03-08 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210308_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='milage',
            new_name='Kilometers',
        ),
    ]
