# Generated by Django 3.2 on 2023-06-19 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashSaleProduct', '0006_voucher_limited_price'),
        ('order', '0002_auto_20230223_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='voucher_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashSaleProduct.voucher'),
        ),
    ]
