# Generated by Django 4.1.5 on 2023-04-18 09:31

import builtins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0007_customer_user_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, serialize=builtins.id, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='cust',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, serialize=builtins.id, to='App.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, serialize=builtins.id, to='App.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
