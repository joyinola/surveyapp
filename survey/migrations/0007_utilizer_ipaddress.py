# Generated by Django 3.2.13 on 2022-05-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_rename_republican_utilizer_party'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizer',
            name='ipAddress',
            field=models.CharField(default='null', max_length=250),
            preserve_default=False,
        ),
    ]