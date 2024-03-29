# Generated by Django 4.2.2 on 2023-06-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_person_alter_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="name_en",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="name_ru",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="profession_en",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="profession_ru",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="surname_en",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="surname_ru",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
