# Generated by Django 3.2 on 2023-07-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cod',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
