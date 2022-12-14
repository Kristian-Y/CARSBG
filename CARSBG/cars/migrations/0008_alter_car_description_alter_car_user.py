# Generated by Django 4.1.3 on 2022-12-11 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0007_alter_car_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
