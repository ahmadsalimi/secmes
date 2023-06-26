# Generated by Django 4.1.1 on 2023-06-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("messenger", "0004_chatrequest"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="chatrequest",
            index=models.Index(
                fields=["requester", "requestee"], name="messenger_c_request_81706a_idx"
            ),
        ),
    ]
