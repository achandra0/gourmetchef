# Generated by Django 2.1.5 on 2020-10-23 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201023_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Offer'),
        ),
    ]
