# Generated by Django 5.0.1 on 2024-01-26 06:46

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
        ('operators', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ism', models.CharField(max_length=30)),
                ('ish_vaqti', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('user.customer',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'active'), ('olindi', 'olindi'), ('boshlandi', 'boshlandi'), ('yakunlandi', 'yakunlandi'), ('bekor qilindi', 'bekor qilindi')], max_length=20)),
                ('total_sum', models.PositiveIntegerField()),
                ('waiting_seconds', models.PositiveSmallIntegerField(default=0)),
                ('baggage', models.BooleanField(default=False)),
                ('for_women', models.BooleanField(default=False)),
                ('starting_point', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('izoh', models.CharField(blank=True, max_length=100, null=True)),
                ('grade', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operators.client')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drivers.driver')),
            ],
        ),
    ]
