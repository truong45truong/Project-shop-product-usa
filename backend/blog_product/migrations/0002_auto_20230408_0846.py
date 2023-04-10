# Generated by Django 3.2 on 2023-04-08 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_delete_heart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.product'),
        ),
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('blog_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hearts', to='blog_product.blog')),
                ('comment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hearts', to='blog_product.comment')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hearts', to='product.product')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hearts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
