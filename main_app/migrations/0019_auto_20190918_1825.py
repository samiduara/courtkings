# Generated by Django 2.2.3 on 2019-09-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20190918_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='owner_points',
            field=models.IntegerField(null=True),
        ),
    ]
