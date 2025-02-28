# Generated by Django 4.0.6 on 2025-02-27 17:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20, verbose_name='имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='адрес')),
                ('desired_date', models.DateTimeField(verbose_name='дата')),
                ('desired_time', models.TimeField(verbose_name='время')),
                ('comment', models.TextField(blank=True, max_length=200, null=True, verbose_name='комментарии к торту')),
                ('deliver_comment', models.TextField(blank=True, max_length=200, null=True, verbose_name='комментарии курьеру')),
                ('total_cost', models.FloatField(default=0.0, verbose_name='общая стоимость')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2025, 2, 27, 17, 39, 8, 965371, tzinfo=utc), verbose_name='дата создания заказа')),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cake.cake', verbose_name='торт')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='cake.client', verbose_name='клиент')),
            ],
        ),
    ]
