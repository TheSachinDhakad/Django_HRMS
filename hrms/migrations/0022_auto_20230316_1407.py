# Generated by Django 2.2.13 on 2023-03-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0021_auto_20230316_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emp_id',
            field=models.CharField(default='emp705', max_length=70),
        ),
    ]
