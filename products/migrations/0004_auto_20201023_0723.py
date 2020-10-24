# Generated by Django 2.1.5 on 2020-10-23 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201023_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='product_name',
        ),
        migrations.AddField(
            model_name='product',
            name='offer_code',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Offer'),
            preserve_default=False,
        ),
    ]
