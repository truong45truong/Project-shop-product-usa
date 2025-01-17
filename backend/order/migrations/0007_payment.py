# Generated by Django 3.2 on 2023-07-11 13:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20230710_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.BooleanField()),
                ('total_price', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='order.order')),
            ],
        ),
    ]
