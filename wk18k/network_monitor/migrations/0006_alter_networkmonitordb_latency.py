# Generated by Django 4.2.5 on 2023-09-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network_monitor', '0005_networkmonitordb_latency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkmonitordb',
            name='latency',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
