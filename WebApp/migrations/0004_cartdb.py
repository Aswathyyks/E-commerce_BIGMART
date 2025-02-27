# Generated by Django 5.1.3 on 2024-12-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_rename_cpwd_registerdb_confirmpwd_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('pro_name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('pro_image', models.ImageField(blank=True, null=True, upload_to='cart_images')),
            ],
        ),
    ]
