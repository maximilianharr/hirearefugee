# Generated by Django 3.1 on 2020-08-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userclass', '0004_auto_20200812_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='is_refugee',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='rating_num',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='rating_val',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
