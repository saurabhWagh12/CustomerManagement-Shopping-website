# Generated by Django 4.1.5 on 2023-04-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_order_cust_order_prod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='App.tag'),
        ),
    ]
