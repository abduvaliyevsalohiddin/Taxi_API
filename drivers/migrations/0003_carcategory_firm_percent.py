# Generated by Django 5.0.1 on 2024-02-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_alter_driver_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='carcategory',
            name='firm_percent',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
