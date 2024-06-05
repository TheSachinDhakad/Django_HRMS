# Generated by Django 4.1.7 on 2023-06-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0039_alter_user_designation_alter_user_emp_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="Date_of_joining",
            field=models.DateField(
                help_text="Please choose a date",
                null=True,
                verbose_name="Select a date",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp576", max_length=70),
        ),
    ]
