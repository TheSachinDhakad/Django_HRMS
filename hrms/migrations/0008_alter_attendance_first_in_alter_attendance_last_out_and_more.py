# Generated by Django 4.1.7 on 2023-03-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0007_alter_user_emp_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="first_in",
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="last_out",
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp550", max_length=70),
        ),
    ]
