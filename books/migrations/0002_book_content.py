# Generated by Django 5.0.3 on 2024-03-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="content",
            field=models.TextField(default="test1"),
            preserve_default=False,
        ),
    ]
