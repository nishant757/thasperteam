# Generated by Django 3.0 on 2020-05-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='phone',
            field=models.TextField(max_length=10, null=True),
        ),
    ]