# Generated by Django 4.1.7 on 2023-02-25 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
