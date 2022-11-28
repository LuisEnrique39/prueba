# Generated by Django 4.1.3 on 2022-11-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instalacionapp", "0005_alter_contrata_numero"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contacto",
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
                ("Nombre", models.FloatField(max_length=20, null=True)),
                ("email", models.CharField(max_length=30, null=True)),
                ("mensaje", models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
