# Generated by Django 4.2 on 2023-06-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0011_order_created_at_order_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
