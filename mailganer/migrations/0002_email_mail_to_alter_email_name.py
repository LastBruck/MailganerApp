# Generated by Django 4.1 on 2022-11-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailganer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="mail_to",
            field=models.CharField(
                default="SOME STRING", max_length=50, verbose_name="eMail"
            ),
        ),
        migrations.AlterField(
            model_name="email",
            name="name",
            field=models.CharField(max_length=50, verbose_name="ФИО"),
        ),
    ]
