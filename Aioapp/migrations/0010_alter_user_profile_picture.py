# Generated by Django 4.2.5 on 2024-02-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aioapp', '0009_rename_username_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='\\media\\profile_pics\\profile.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
