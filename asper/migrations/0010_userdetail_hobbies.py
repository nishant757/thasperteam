# Generated by Django 3.0 on 2020-05-13 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0009_firsttask'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='hobbies',
            field=models.TextField(max_length=30, null=True),
        ),
    ]