# Generated by Django 5.1.3 on 2024-11-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cat_des', models.CharField(blank=True, max_length=100, null=True)),
                ('cat_image', models.ImageField(blank=True, null=True, upload_to='Category_Image')),
            ],
        ),
    ]
