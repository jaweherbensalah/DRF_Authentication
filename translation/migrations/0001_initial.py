# Generated by Django 4.2.2 on 2023-06-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("title_ru", models.CharField(max_length=200, null=True)),
                ("about", models.CharField(max_length=200)),
                ("about_en", models.CharField(max_length=200, null=True)),
                ("about_ru", models.CharField(max_length=200, null=True)),
            ],
        ),
    ]