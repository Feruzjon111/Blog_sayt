# Generated by Django 5.1.2 on 2025-04-06 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=500, null=True)),
                ("username", models.CharField(blank=True, max_length=200, null=True)),
                ("location", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "short_intro",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="profiles/user-default.png",
                        null=True,
                        upload_to="profiles/",
                    ),
                ),
                (
                    "social_github",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_twitter",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_linkedin",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_youtube",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_website",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                ("subject", models.CharField(blank=True, max_length=200, null=True)),
                ("is_read", models.BooleanField(default=False, null=True)),
                ("body", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "recipient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="messages",
                        to="account.profile",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="account.profile",
                    ),
                ),
            ],
            options={
                "ordering": ["is_read", "-created"],
            },
        ),
        migrations.CreateModel(
            name="Skill",
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
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.profile",
                    ),
                ),
            ],
        ),
    ]
