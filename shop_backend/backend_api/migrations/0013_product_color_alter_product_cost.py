# Generated by Django 4.2 on 2023-07-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0012_alter_product_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('red', 'Красный'), ('yellow', 'Желтый'), ('blue', 'Синий'), ('black', 'черный'), ('white', 'белый'), ('default', 'другое')], default='другое', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
