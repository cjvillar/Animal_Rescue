# Generated by Django 4.1.1 on 2022-09-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal_rescue_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="image",
            field=models.ImageField(default=None, upload_to="profile_images"),
        ),
    ]
