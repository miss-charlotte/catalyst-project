# Generated by Django 4.2 on 2023-04-27 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapp', '0008_delete_recentorders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='expiredQuantity',
        ),
    ]
