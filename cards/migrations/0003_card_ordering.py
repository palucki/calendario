# Generated by Django 5.0 on 2023-12-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_calendar_options_card_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='ordering',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]