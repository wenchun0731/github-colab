# Generated by Django 5.0.6 on 2024-05-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='violation',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False),
        ),
    ]
