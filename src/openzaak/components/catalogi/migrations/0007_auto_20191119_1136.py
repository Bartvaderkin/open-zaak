# Generated by Django 2.2.4 on 2019-11-19 11:36

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogi", "0006_auto_20191024_1000"),
    ]

    operations = [
        migrations.AlterField(
            model_name="besluittype",
            name="zaaktypes",
            field=models.ManyToManyField(
                help_text="ZAAKTYPE met ZAAKen die relevant kunnen zijn voor dit BESLUITTYPE",
                related_name="besluittypen",
                to="catalogi.ZaakType",
                verbose_name="zaaktypen",
            ),
        ),
        migrations.RenameField(
            model_name="besluittype", old_name="zaaktypes", new_name="zaaktypen",
        ),
        migrations.AlterField(
            model_name="informatieobjecttype",
            name="zaaktypes",
            field=models.ManyToManyField(
                help_text="ZAAKTYPE met ZAAKen die relevant kunnen zijn voor dit INFORMATIEOBJECTTYPE",
                related_name="informatieobjecttypen",
                through="catalogi.ZaakInformatieobjectType",
                to="catalogi.ZaakType",
                verbose_name="zaaktypen",
            ),
        ),
        migrations.RenameField(
            model_name="informatieobjecttype",
            old_name="zaaktypes",
            new_name="zaaktypen",
        ),
    ]