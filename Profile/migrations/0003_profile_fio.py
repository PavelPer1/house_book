# Generated by Django 4.1.4 on 2023-07-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fio',
            field=models.CharField(max_length=100, null=True),
        ),
    ]