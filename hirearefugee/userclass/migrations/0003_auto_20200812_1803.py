# Generated by Django 3.1 on 2020-08-12 18:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userclass', '0002_auto_20200812_1731'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserClass',
            new_name='UserDetails',
        ),
    ]
