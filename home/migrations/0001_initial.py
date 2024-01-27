# Generated by Django 5.0.1 on 2024-01-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "custom_session",
            },
        ),
    ]
