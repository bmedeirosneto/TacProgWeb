# Generated by Django 2.2.7 on 2019-11-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecampus', '0005_auto_20191121_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sutia',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
