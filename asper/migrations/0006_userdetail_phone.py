# Generated by Django 3.0 on 2020-05-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0005_remove_userdetail_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
