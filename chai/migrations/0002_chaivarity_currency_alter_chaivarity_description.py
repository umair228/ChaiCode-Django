# Generated by Django 4.2.13 on 2024-05-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chai", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chaivarity",
            name="currency",
            field=models.CharField(default="PKR", max_length=3),
        ),
        migrations.AlterField(
            model_name="chaivarity",
            name="description",
            field=models.TextField(default="empty"),
        ),
    ]
