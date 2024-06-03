# Generated by Django 4.2.7 on 2024-05-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0008_alter_product_time_span"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="cert",
            field=models.CharField(
                blank=True,
                choices=[
                    ("BRC", "BRC Standard"),
                    ("COSMOS", "COSMOS Organic and Natural"),
                    ("CFC", "Cruelty Free Certificate"),
                    ("EnergyStar", "Energy Star"),
                    ("FairTradeCertificate", "Fair Trade Certificate"),
                    ("FCC", "FCC Certificate"),
                    ("FSC", "FSC Certificate"),
                    ("GOTS", "GOTS Certificcate"),
                    ("HACCP", "HACCP"),
                    ("HALAL", "HALAL Certificate"),
                    ("ISO9001", "ISO 9001"),
                    ("ISO14001", "ISO 14001"),
                    ("ISO22000", "ISO 22000"),
                    ("ISO_TS", "ISO_TS 16949"),
                    ("Kosher", "Kosher"),
                    ("Non-GMO", "Non-GMO Certificate"),
                    ("RoHS", "RoHS Compliance"),
                    ("Wrap", "Wrap Certificate"),
                    ("Other", "Other"),
                ],
                max_length=250,
                null=True,
                verbose_name="Certification Name",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="order_unit",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Kilogram", "Kilogram"),
                    ("Litre", "Litre"),
                    ("Pack", "Pack"),
                    ("Set", "Set"),
                    ("Ton", "Ton"),
                ],
                max_length=250,
                null=True,
                verbose_name="Measure",
            ),
        ),
    ]
