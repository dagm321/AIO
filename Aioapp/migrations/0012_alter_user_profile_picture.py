# Generated by Django 4.2.5 on 2024-02-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aioapp', '0011_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
