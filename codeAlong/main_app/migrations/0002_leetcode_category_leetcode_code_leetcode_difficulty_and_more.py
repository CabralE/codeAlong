# Generated by Django 4.1.5 on 2023-01-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leetcode',
            name='category',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leetcode',
            name='code',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leetcode',
            name='difficulty',
            field=models.CharField(default=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leetcode',
            name='link',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leetcode',
            name='name',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leetcode',
            name='study_solution',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leetcode',
            name='video_solution',
            field=models.CharField(default=True, max_length=30),
            preserve_default=False,
        ),
    ]
