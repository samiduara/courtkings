# Generated by Django 2.2.3 on 2019-09-18 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20190918_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
