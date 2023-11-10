# Generated by Django 4.2.6 on 2023-11-08 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField(blank=True, null=True)),
                ('model_year', models.IntegerField(blank=True, null=True)),
                ('plate', models.CharField(blank=True, max_length=10, null=True)),
                ('value', models.FloatField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cars/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand')),
            ],
        ),
    ]
