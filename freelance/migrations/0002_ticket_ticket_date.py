# Generated by Django 3.0.5 on 2020-10-01 23:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
