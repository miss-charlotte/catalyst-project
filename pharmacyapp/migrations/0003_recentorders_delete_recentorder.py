# Generated by Django 4.2 on 2023-04-26 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapp', '0002_recentorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='pharmacyapp.sale')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='pharmacyapp.sale')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='pharmacyapp.product')),
                ('quantityBought', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quantities', to='pharmacyapp.sale')),
            ],
        ),
        migrations.DeleteModel(
            name='RecentOrder',
        ),
    ]
