# Generated by Django 5.1.3 on 2024-12-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_orderdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdb',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
