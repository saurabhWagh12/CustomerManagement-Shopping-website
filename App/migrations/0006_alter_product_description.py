# Generated by Django 4.1.5 on 2023-04-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_remove_order_tag_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
