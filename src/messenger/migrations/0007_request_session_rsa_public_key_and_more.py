# Generated by Django 4.1.1 on 2023-06-28 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("messenger", "0006_groupchat_groupchatmember_groupchat_members"),
    ]

    operations = [
        migrations.CreateModel(
            name="Request",
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
                ("request_id", models.UUIDField(blank=True, null=True)),
                ("request_type", models.CharField(max_length=256)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="session",
            name="rsa_public_key",
            field=models.BinaryField(default=None),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="groupchatmember", unique_together={("user", "group_chat")},
        ),
        migrations.AddIndex(
            model_name="groupchatmember",
            index=models.Index(
                fields=["user", "group_chat"], name="messenger_g_user_id_4d349e_idx"
            ),
        ),
        migrations.AddField(
            model_name="request",
            name="requester",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="requests_sent",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
