# Generated by Django 5.0.7 on 2024-07-16 11:23

import django.contrib.postgres.fields
import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authentik_policies", "0011_policybinding_failure_result_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="GeoIPPolicy",
            fields=[
                (
                    "policy_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_policies.policy",
                    ),
                ),
                (
                    "asns",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), blank=True, default=list, size=None
                    ),
                ),
                (
                    "countries",
                    django_countries.fields.CountryField(blank=True, max_length=746, multiple=True),
                ),
            ],
            options={
                "verbose_name": "GeoIP Policy",
                "verbose_name_plural": "GeoIP Policies",
                "indexes": [
                    models.Index(fields=["policy_ptr_id"], name="authentik_p_policy__5cc4a9_idx")
                ],
            },
            bases=("authentik_policies.policy",),
        ),
    ]