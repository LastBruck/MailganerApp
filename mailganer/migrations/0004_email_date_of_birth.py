# Generated by Django 4.1 on 2022-11-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailganer", "0003_alter_email_options_email_track"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="date_of_birth",
            field=models.CharField(
                default="SOME STRING", max_length=10, verbose_name="День рождения"
            ),
        ),
    ]