# Generated by Django 4.1.7 on 2023-02-22 06:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0002_auto_20230126_1156"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="bank",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="nuban",
        ),
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.TextField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="hrms.department",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="emergency",
            field=models.CharField(default=2, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp798", max_length=70),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("male", "MALE"), ("female", "FEMALE"), ("other", "OTHER")],
                default=54,
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[
                    ("english", "ENGLISH"),
                    ("yoruba", "YORUBA"),
                    ("hausa", "HAUSA"),
                    ("french", "FRENCH"),
                ],
                default="english",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="mobile",
            field=models.CharField(default=1223456, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="salary",
            field=models.CharField(default="00,000.00", max_length=16),
        ),
        migrations.AlterField(
            model_name="employee",
            name="emp_id",
            field=models.CharField(default="emp127", max_length=70),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=125),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="thumb",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
