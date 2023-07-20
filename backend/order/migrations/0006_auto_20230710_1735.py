# Generated by Django 3.2 on 2023-07-10 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_confirm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qrcode', models.ImageField(blank=True, upload_to='static/qrcode')),
                ('name', models.CharField(max_length=20)),
                ('token', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='qr_code_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.qrcode'),
        ),
    ]