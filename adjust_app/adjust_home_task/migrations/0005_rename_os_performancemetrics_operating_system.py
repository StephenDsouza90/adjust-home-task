# Generated by Django 3.2 on 2021-04-27 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adjust_home_task', '0004_alter_performancemetrics_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performancemetrics',
            old_name='os',
            new_name='operating_system',
        ),
    ]