# Generated by Django 3.2.10 on 2023-03-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcamera', '0005_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(max_length=100),
        ),
    ]
