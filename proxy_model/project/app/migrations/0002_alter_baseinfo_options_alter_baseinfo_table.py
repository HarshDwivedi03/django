# Generated by Django 5.2 on 2025-04-24 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseinfo',
            options={'ordering': ['id'], 'verbose_name': 'My custom Model', 'verbose_name_plural': 'My custom Model'},
        ),
        migrations.AlterModelTable(
            name='baseinfo',
            table='student',
        ),
    ]
