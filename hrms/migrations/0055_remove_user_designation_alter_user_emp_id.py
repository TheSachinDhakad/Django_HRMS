# Generated by Django 4.1.7 on 2023-06-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0054_alter_user_designation_alter_user_emp_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="Designation",
        ),
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp219", max_length=70),
        ),
    ]
