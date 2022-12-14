# Generated by Django 4.1.3 on 2022-11-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=15)),
                ('car_model', models.CharField(max_length=30)),
                ('engine', models.CharField(max_length=30)),
                ('type_of_fuel', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=150)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('images', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
