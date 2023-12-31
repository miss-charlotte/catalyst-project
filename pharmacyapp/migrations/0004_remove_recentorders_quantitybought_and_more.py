# Generated by Django 4.2 on 2023-04-26 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pharmacyapp', '0003_recentorders_delete_recentorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recentorders',
            name='quantityBought',
        ),
        migrations.AddField(
            model_name='recentorders',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recentorders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recentorders',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recentorders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.product'),
        ),
    ]
