# Generated by Django 4.1.5 on 2023-04-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_customer_date_alter_customer_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
