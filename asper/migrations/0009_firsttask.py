# Generated by Django 3.0 on 2020-05-11 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asper', '0008_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q1', models.TextField(max_length=100, null=True)),
                ('Q2', models.TextField(max_length=100, null=True)),
                ('Q3', models.TextField(max_length=100, null=True)),
                ('Q4', models.TextField(max_length=100, null=True)),
                ('Q5', models.TextField(max_length=100, null=True)),
                ('Q6', models.TextField(max_length=100, null=True)),
                ('Q7', models.TextField(max_length=100, null=True)),
                ('Q8', models.TextField(max_length=100, null=True)),
                ('usr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
