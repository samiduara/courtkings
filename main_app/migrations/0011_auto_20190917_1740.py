# Generated by Django 2.2.3 on 2019-09-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20190917_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='roster',
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(null=True, to='main_app.Player'),
        ),
    ]
