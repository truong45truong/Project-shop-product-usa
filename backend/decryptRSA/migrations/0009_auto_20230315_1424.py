# Generated by Django 3.2 on 2023-03-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decryptRSA', '0008_deviceclient_name_private_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceclient',
            name='name_private_key',
        ),
        migrations.AlterField(
            model_name='deviceclient',
            name='public_key',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
