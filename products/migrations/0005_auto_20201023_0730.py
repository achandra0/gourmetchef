# Generated by Django 2.1.5 on 2020-10-23 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201023_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Offer'),
        ),
    ]
