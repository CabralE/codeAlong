# Generated by Django 4.0.1 on 2023-01-08 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_leetcode_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leetcode',
            name='user',
        ),
    ]
