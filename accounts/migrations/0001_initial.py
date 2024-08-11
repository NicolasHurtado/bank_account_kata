# Generated by Django 5.1 on 2024-08-09 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("iban", models.CharField(max_length=34, unique=True)),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("deposit", "Deposit"),
                            ("withdrawal", "Withdrawal"),
                            ("transfer", "Transfer"),
                        ],
                        max_length=10,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("balance_after", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="accounts.account",
                    ),
                ),
            ],
        ),
    ]
