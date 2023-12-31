# Generated by Django 4.1.7 on 2023-04-25 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicineName', models.CharField(blank=True, max_length=50, null=True)),
                ('quantityinStore', models.IntegerField(default=0)),
                ('receivedQuantity', models.IntegerField(default=0)),
                ('quantitySold', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('expiredQuantity', models.IntegerField(default=0)),
                ('unitCost', models.IntegerField(default=0)),
                ('expiryDate', models.DateField(blank=True, null=True)),
                ('categoryName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('amountPaid', models.IntegerField(default=0)),
                ('boughtBy', models.CharField(blank=True, max_length=50, null=True)),
                ('unitCost', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.product')),
            ],
        ),
    ]
